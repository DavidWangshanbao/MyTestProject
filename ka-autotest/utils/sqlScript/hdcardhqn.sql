----------总部普通库
----------start
create database link link_pos4
  connect to HD40
  identified by "hd40"
  using '(DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 172.17.12.22)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = hdpos4)
    )
  )';
----------end
----------start
create table IMPDataResult(CLS varchar2(100),UUID varchar2(100),RET integer,CONTENT varchar2(1000),FILDATE DATE);
----------end
----------start
create or replace package POS_STORE_CARD is

  ---门店资料到总部普通库--调用程序
  function ImpStore(poErrMsg out varchar2) return number;

  ---将门店资料从总部复制到卡中心--调用程序
  function ImpStoreHQToCenter(poErrMsg out varchar2) return number;

  function NextLevelId(piStoreLevelId in int) return varchar2;            --

  ---门店资料总部写入--主程序
  function StoreHQInsert(
    piStoreCode in varchar2,
    piStoreName in varchar2,
    /*pistoretypeuuid in cardadminstore.storetypeuuid%type,
    pistoretypecode in cardadminstore.storetypecode%type,
    pistoretypename in cardadminstore.storetypename%type,*/
    piAClevelid in RBAdminCenter.Levelid%type,
    piLevelId in Tangodomain.Levelid%type,
    piUpperDomainUuid Tangodomain.Uuid%type,
    piEmpCenterUuid Rborganization.Empcenteruuid%type,
    piUpperOrganization Rborganization.Upperorganization%type,
    piIp Department.v_Ip%type,
    piPort Department.v_Port%type,
    piAdminCenter RBAdminCenter.uuid%type,
    poErrMsg out varchar2) return number;

  ---将门店资料从总部复制到卡中心--主程序
  function StoreHQToCenterInsert(piStoreCode in Rborganization.Code%type,poErrMsg out varchar2)return number;

end POS_STORE_CARD;
----------end
----------start
create or replace package body POS_STORE_CARD is
--生成uuid函数
  function GenUUID return varchar2 is
  begin
    return sys_guid();
  end;
--记录日志
  procedure AddLog(
    piCls in varchar2,
    piUUID in varchar2,
    piResult in integer,
    piContent in varchar2) is
  begin
    insert into IMPDataResult(Cls, Ret, Content, UUID)
    values(piCls, piResult, piContent, piUUID);
    commit;
  end;

--生成级别ID
  function NextLevelId(piStoreLevelId in int) return varchar2 is
    Len           number;
    levelIdLen    number;
    vStoreLevelId varchar2(100);
  begin
    Len           := 4;
    vStoreLevelId := to_char(piStoreLevelId);
    levelIdLen    := Length(vStoreLevelId);

    while levelIdLen < Len loop
      vStoreLevelId := '0' || vStoreLevelId;
      levelIdLen    := Length(vStoreLevelId);
    end loop;
    return(vStoreLevelId);
  end;
----------------------------------------------------------------------------------
  -----------脚本执行说明 导入门店信息--------------
  -- 1. 脚本需要在总部的普通库中执行
  -- 2. 创建dblink
  -- 4. 使用的中心代码默认为1111，需要根据现场部署修改
function ImpStore(poErrMsg out varchar2) return number
  is
    vAClevelid  RBAdminCenter.Levelid%type;
    vLevelId Tangodomain.Levelid%type;
    vDomainUuid Tangodomain.Uuid%type;
    vEmpCenterUuid Rborganization.Empcenteruuid%type;
    vOrganization Rborganization.Uuid%type;
    vIp Department.v_Ip%type;
    vPort Department.v_Port%type;
    vAdminCenter RBAdminCenter.uuid%type;

    vCenterCode Tangodomain.Code%type;
    iStoreLevelId int;

    vRet int;
    vHasCardNum int;
    vCode varchar2(20);
    vName varchar2(100);
/*    vstoretypeuuid  cardadminstore.storetypeuuid%type;
    vstoretypecode  cardadminstore.storetypecode%type;
    vstoretypename  cardadminstore.storetypename%type;*/
    /**加入门店类型 edit by quyi 20130905**/
    cursor c_StoreInfo is
        select s.code,s.name from store@LINK_POS4 s   --需要修改中间表表名 9723
         /* left join cardoptioninfo op
            on s.storebrand = op.name*/
         where /*op.type='STORETYPE' and*/ s.code not in ('8888','9999');
  begin
    vCenterCode := '8888'; --需要根据现场部署修改 卡中心代码
    iStoreLevelId := 0;
  ADDLOG('ImpStoreBegin', '-', 0, '门店资料开始导入...');

    select levelId, uuid into vLevelId, vDomainUuid
    from Tangodomain
    where code = vCenterCode;

    select empCenterUuid, uuid into vEmpCenterUuid, vOrganization
    from Rborganization
    where code = vCenterCode;

    select uuid,levelid into vAdminCenter,vAClevelid
    from RBAdminCenter
    where Organization = vOrganization;

    select d.v_ip, d.v_port into vIp, vPort
    from Department d, Rborganization o
    where d.organization = o.uuid and o.code = vCenterCode;
    for curDtl in c_StoreInfo loop
      vCode := curDtl.code;
      vName := curDtl.Name;
      /*vstoretypeuuid := curDtl.storetypeuuid;
      vstoretypecode := curDtl.storetypecode;
      vstoretypename := curDtl.storetypename;*/

      select count(uuid) into vHasCardNum
      from Rborganization o
      where o.code = vCode;

      if (vHasCardNum = 0) then
        vRet := StoreHQInsert(vCode, vName,/*vstoretypeuuid,vstoretypecode,vstoretypename,*/vAClevelid || NextLevelId(iStoreLevelId),vLevelId || NextLevelId(iStoreLevelId), vDomainUuid,
                  vEmpCenterUuid, vOrganization, vIp, vPort, vAdminCenter, poErrMsg);

        if (vRet = 0) then
          ADDLOG('QS_ImpStore', vCode, vRet, '门店资料导入HDCARD成功');
        elsif (vRet = 1) then
          ADDLOG('QS_ImpStore', vCode, vRet, '门店资料导入HDCARD失败 ' || poErrMsg);
        end if;
        iStoreLevelId := iStoreLevelId + 1;
      else
         ADDLOG('ImpStore', vCode, 2, '门店资料在HDCARD数据库中已经存在');
        /* update CardAdminStore t
            set t.storetypeuuid = vstoretypeuuid,
                t.storetypecode = vstoretypecode,
                t.storetypename = vstoretypename
          where t.organization =
                (select uuid from rborganization o where o.code = vcode);
        ADDLOG('BJ_UpdateHeadquarterStoreType', vCode, 2, '门店资料门店类型更新完成');*/
      end if;
    end loop;
  ADDLOG('ImpStoreEnd', '-', 0, '门店资料导入完成!');
    return(0);
  end;

--将门店信息插入总部
function StoreHQInsert(
    piStoreCode in varchar2,
    piStoreName in varchar2,
    /*pistoretypeuuid in cardadminstore.storetypeuuid%type,
    pistoretypecode in cardadminstore.storetypecode%type,
    pistoretypename in cardadminstore.storetypename%type,*/

    piAClevelid in RBAdminCenter.Levelid%type,
    piLevelId in Tangodomain.Levelid%type,
    piUpperDomainUuid Tangodomain.Uuid%type,
    piEmpCenterUuid Rborganization.Empcenteruuid%type,
    piUpperOrganization Rborganization.Upperorganization%type,
    piIp Department.v_Ip%type,
    piPort Department.v_Port%type,
    piAdminCenter RBAdminCenter.uuid%type,
    poErrMsg out varchar2) return number
  is
    vStoreCode         varchar2(100); --
    vStoreName         varchar2(100); --
    /*vstoretypeuuid     cardadminstore.storetypeuuid%type;
    vstoretypecode     cardadminstore.storetypecode%type;
    vstoretypename     cardadminstore.storetypename%type;*/

    vAClevelid         RBAdminCenter.Levelid%type;
    vLevelId           Tangodomain.Levelid%type;
    vUpperDomainUuid   Tangodomain.Uuid%type;
    vEmpCenterUuid     Rborganization.Empcenteruuid%type;
    vUpperOrganization Rborganization.Upperorganization%type;
    vIp                Department.v_Ip%type;
    vPort              Department.v_Port%type;
    vAdminCenter       RBAdminCenter.uuid%type;

    vDepUuid              Department.Uuid%type;
    vCardStoreUuid        CardAdminStore.Uuid%type;
    vAdminUnitUuid        RBAdminUnit.Uuid%type;
    vRbOrganizationUuid   Rborganization.Uuid%type;
    vTangoDomainUuid      Tangodomain.Uuid%type;
    vRBDomainFuncViewUnitUuid RBDomainFuncView.Uuid%type;
    vRBDomainFuncViewStoreUuid RBDomainFuncView.Uuid%type;
    vRBOrgRoleProxyUnitUuid   RBOrgRoleProxy.Uuid%type;
    vRBOrgRoleProxyStoreUuid   RBOrgRoleProxy.Uuid%type;
    vOrgOrgTypeUuid            Rborgorgtype.Uuid%type;
    vRemark varchar2(100);
  begin
    begin
      vStoreCode         := piStoreCode;
      vStoreName         := piStoreName;
     /* vstoretypeuuid     := pistoretypeuuid;
      vstoretypecode     := pistoretypecode;
      vstoretypename     := pistoretypename;*/

      vAClevelid         := piAClevelid;
      vLevelId           := piLevelId;
      vUpperDomainUuid   := piUpperDomainUuid;
      vEmpCenterUuid     := piEmpCenterUuid;
      vUpperOrganization := piUpperOrganization;
      vIp                := piIp;
      vPort              := piPort;
      vAdminCenter       := piAdminCenter;

      vDepUuid                  := GenUUID;
      vCardStoreUuid            := GenUUID;
      vAdminUnitUuid            := GenUUID;
      vRBOrganizationUuid       := GenUUID;
      vTangoDomainUuid          := GenUUID;
      vRBDomainFuncViewUnitUuid := GenUUID;
      vRBDomainFuncViewStoreUuid:= GenUUID;
      vRBOrgRoleProxyUnitUuid   := GenUUID;
      vRBOrgRoleProxyStoreUuid  := GenUUID;
      vOrgOrgTypeUuid           := GenUUID;

      vRemark := '分公司门店导入';   --edit by fx 130618

      --插入组织角色代理
      insert into RBOrgRoleProxy(UUID, STATE, ORGROLEUUID, ORGROLECLASSNAME, ORGANIZATION, ISSUPER, REFCOUNT)
      values (vRBOrgRoleProxyUnitUuid,'0',vAdminUnitUuid,'com.hd123.rumba.ejb.orgrole.admin.AdminUnit', vRBOrganizationUuid, 0, 1);
       insert into RBOrgRoleProxy(UUID, STATE, ORGROLEUUID, ORGROLECLASSNAME, ORGANIZATION, ISSUPER, REFCOUNT)
      values (vRBOrgRoleProxyStoreUuid,'0',vCardStoreUuid,'com.hd123.card.ejb.admin.store.AdminStore', vRBOrganizationUuid, 0, 0);

      -- 插入域功能视图
      insert into RBDomainFuncView (UUID, IMPLEMENTATION, FUNCVIEW, DOMAIN, FCAUSE)
      values (vRBDomainFuncViewUnitUuid, 'com.hd123.rumba.domain.DomainFuncView','RBAU', vTangoDomainUuid, 'com.hd123.rumba.ejb.orgrole.admin.AdminUnit');
      insert into RBDomainFuncView (UUID, IMPLEMENTATION, FUNCVIEW, DOMAIN, FCAUSE)
      values (vRBDomainFuncViewStoreUuid, 'com.hd123.rumba.domain.DomainFuncView','CARDST', vTangoDomainUuid, 'com.hd123.card.ejb.admin.store.AdminStore');

      -- 插入域
      insert into Tangodomain (UUID, LASTMODIFIED, LASTMODIFIER, OCA, NAME,
         STATE, IMPLEMENTATION, CODE, REMARK, LEVELID,
         UPPERDOMAIN, DOMAIN,Created,Creator)
      values (vTangoDomainUuid, sysdate, '管理员用户[admin@9999]', '0', vStoreName,
         '0', 'com.hd123.rumba.domain.Domain', vStoreCode, vRemark, vLevelId,
         vUpperDomainUuid, 'ROOT',sysdate,'管理员用户[admin@9999]');

      -- 插入组织
      insert into RBOrganization (UUID, LASTMODIFIED, OCA, LASTMODIFIER, DOMAIN,
         NAME, STATE, IMPLEMENTATION, CODE, REMARK,
         ORGANIZATIONDOMAIN, LEVELID, EMPCENTERUUID, UPPERORGANIZATION)
      values (vRbOrganizationUuid, sysdate, '0', '管理员用户[admin@9999]', 'ROOT',
         vStoreName, '0', 'com.hd123.rumba.organization.Organization', vStoreCode, vRemark,
         vTangoDomainUuid, vLevelId, vEmpCenterUuid, vUpperOrganization);

      -- 插入组织组织类型关系
      insert into RBOrgOrgType (UUID, STATE, ORGANIZATION, ORGTYPE)
      values (vOrgOrgTypeUuid, '0', vRbOrganizationUuid, 'store-orgtype-uuid');

      -- 插入行政管理单位
      insert into RBAdminUnit (UUID, LASTMODIFIED, OCA, LASTMODIFIER, DOMAIN,
          STATE, ORGANIZATION, UPPER, ADMINCENTER,LEVELID)
      values (vAdminUnitUuid, sysdate, '0',  '管理员用户[admin@9999]', 'ROOT',
          '0', vRbOrganizationUuid, vAdminCenter, vAdminCenter,vAClevelid);

      -- 插入门店
      insert into CardAdminStore (UUID, LASTMODIFIED, OCA, LASTMODIFIER, ADMINFUNCTION,
          DOMAIN, STATE, ORGANIZATION/*, Storetypeuuid, Storetypecode, Storetypename*/)
      values (vCardStoreUuid, sysdate, '0', '管理员用户[admin@9999]', 'REISSUE',
          'ROOT', '0', vRbOrganizationUuid/*, vstoretypeuuid, vstoretypecode, vstoretypename*/);

      -- 插入部门表
      insert into Department (UUID, REMARK, OCA, LASTMODIFYTIME, V_DEPSTATE,
         V_IP, V_DEPTYPE, V_DEPFUNCTION, ORGANIZATION, V_PORT)
      values (vDepUuid, vRemark, '0', sysdate, 'USEABLE',
         vIp, 'STORE', 'REISSUE', vRbOrganizationUuid, vPort);
      commit;
      return(0);
    exception
      when others then
      begin
        rollback;
        poErrMsg := '错误号:' || SQLCODE || ',错误信息:' || SQLERRM;
        return(1);
      end;
    end;
  end;


---------------------------------------------------------------------------------------

   -----------脚本执行说明 从HDCARD总部导入门店信息至中心数据库--------------
  -- 1. 脚本需要在总部的普通库中执行
  -- 2. 创建dblink
  -- 连接至中心普通数据库的dblink名称为LINK_CARDCTNTEST.HDDOMAIN.CN
  -- 3. 使用的中心代码默认为1111，需要根据现场部署修改

  function ImpStoreHQToCenter(poErrMsg out varchar2) return number
  is
    vRet int;
    vHasStoreCode int;

    cursor c_StoreCode is
      select o.code, o.name,t.storetypeuuid,t.storetypecode,t.storetypename
        from department d, rborganization o, store@LINK_POS4 s,cardadminstore t  --需修改中间表表名
       where d.organization = o.uuid
         and o.code = s.code
         --and o.name = s.name           modify by quyi 20131012  修复对于门店名称不一致导致的不同步问题。
         and t.organization=o.uuid
         and d.v_deptype = 'STORE';
  begin
    ADDLOG('ImpStoreHQToCenterBegin', '-', 0, '门店资料从总部普通库导入中心普通库开始...');
    for curDtl in c_StoreCode loop
      select count(code) into vHasStoreCode
      from Rborganization@LINK_CARDCTN.HDDOMAIN.CN where code = curDtl.code;
      if (vHasStoreCode = 0) then
        vRet := StoreHQToCenterInsert(curDtl.code, poErrMsg);
        if (nvl(vRet,1) = 0) then
          ADDLOG('ImpStoreHQToCenter', curDtl.code, vRet, '门店资料从总部普通库导入中心普通库成功');
        else
          ADDLOG('ImpStoreHQToCenter', curDtl.code, vRet, '门店资料从总部普通库导入中心普通库失败 ' || poErrMsg);
        end if;
      else
        ADDLOG('ImpStoreHQToCenter', curDtl.code, 1, '门店资料在中心普通库中已经存在');
        /*update CardAdminStore@LINK_CARDCTN.HDDOMAIN.CN t
           set t.storetypeuuid = curDtl.storetypeuuid,
               t.storetypecode = curDtl.storetypecode,
               t.storetypename = curDtl.storetypename
         where t.organization =
               (select uuid from rborganization@LINK_CARDCTN.HDDOMAIN.CN o where o.code = curDtl.id);
        ADDLOG('BJ_UpdateCenterStoreType', curDtl.id, 2, '门店资料门店类型更新完成');*/
      end if;
    end loop;
  ADDLOG('ImpStoreHQToCenterEnd', '-', 0, '门店资料从总部普通库导入中心普通库完成！');
    return (0);
  end;

--从总部同步到中心
 --插入
  function StoreHQToCenterInsert(piStoreCode in Rborganization.Code%type,poErrMsg out varchar2)return number is
  vStoreCode Rborganization.Code%type;
  begin
    begin
      vStoreCode := piStoreCode;

      --插入组织角色代理
      insert into RBOrgRoleProxy@LINK_CARDCTN.HDDOMAIN.CN (UUID, STATE, ORGROLEUUID, ORGROLECLASSNAME, ORGANIZATION, ISSUPER, REFCOUNT)
      select r.uuid, r.state, r.orgroleuuid, r.orgroleclassname, r.organization, r.issuper, r.refcount
      from RBOrgRoleProxy r,Rborganization o
      where r.organization = o.uuid and o.code = vStoreCode;

      -- 插入域功能视图
      insert into RBDomainFuncView@LINK_CARDCTN.HDDOMAIN.CN (UUID, IMPLEMENTATION, FUNCVIEW, DOMAIN, FCAUSE)
      select o.UUID, o.IMPLEMENTATION, o.FUNCVIEW, o.DOMAIN, o.FCAUSE
      from RBDomainFuncView o,TangoDomain t
      where o.domain = t.uuid and t.code = vStoreCode;

      -- 插入域
      insert into Tangodomain@LINK_CARDCTN.HDDOMAIN.CN (UUID, LASTMODIFIED, LASTMODIFIER, OCA, NAME,
         STATE, IMPLEMENTATION, CODE, REMARK, LEVELID,
         UPPERDOMAIN, DOMAIN,Created,Creator)
      select UUID, LASTMODIFIED, LASTMODIFIER, OCA, NAME,
        STATE, IMPLEMENTATION, CODE, REMARK, LEVELID,
        UPPERDOMAIN, DOMAIN,Created,Creator
      from TangoDomain where code = vStoreCode;

      -- 插入组织
      insert into RBOrganization@LINK_CARDCTN.HDDOMAIN.CN (UUID, LASTMODIFIED, OCA, LASTMODIFIER, DOMAIN,
         NAME, STATE, IMPLEMENTATION, CODE, REMARK,
         ORGANIZATIONDOMAIN, LEVELID, EMPCENTERUUID, UPPERORGANIZATION)
      select UUID, LASTMODIFIED, OCA, LASTMODIFIER, DOMAIN,
         NAME, STATE, IMPLEMENTATION, CODE, REMARK,
         ORGANIZATIONDOMAIN, LEVELID, EMPCENTERUUID, UPPERORGANIZATION
      from RBOrganization where code = vStoreCode;

      -- 插入组织组织类型关系
      insert into RBOrgOrgType@LINK_CARDCTN.HDDOMAIN.CN (UUID, STATE, ORGANIZATION, ORGTYPE)
      select t.UUID, t.STATE, t.ORGANIZATION, t.ORGTYPE
      from RBOrgOrgType t, Rborganization o
      where t.organization = o.uuid and o.code = vStoreCode;

      -- 插入行政管理单位
      insert into RBAdminUnit@LINK_CARDCTN.HDDOMAIN.CN (UUID, LASTMODIFIED, OCA, LASTMODIFIER, DOMAIN,
          STATE, ORGANIZATION, UPPER, ADMINCENTER, LEVELID)
      select t.UUID, t.LASTMODIFIED, t.OCA, t.LASTMODIFIER, t.DOMAIN,
          t.STATE, t.ORGANIZATION, t.UPPER, t.ADMINCENTER, t.LEVELID
      from RBAdminUnit t, Rborganization o
      where t.organization = o.uuid and o.code = vStoreCode;

      -- 插入门店
      insert into CardAdminStore@LINK_CARDCTN.HDDOMAIN.CN (UUID, LASTMODIFIED, OCA, LASTMODIFIER, ADMINFUNCTION,
          DOMAIN, STATE, ORGANIZATION/*, Storetypeuuid, Storetypecode, Storetypename*/)
      select t.UUID, t.LASTMODIFIED, t.OCA, t.LASTMODIFIER, t.ADMINFUNCTION,
          t.DOMAIN, t.STATE, t.ORGANIZATION/*, t.storetypeuuid, t.storetypecode, t.storetypename*/
      from CardAdminStore t, Rborganization o
      where t.organization = o.uuid and o.code = vStoreCode;

      -- 插入部门表
      insert into Department@LINK_CARDCTN.HDDOMAIN.CN (UUID, REMARK, OCA, LASTMODIFYTIME, V_DEPSTATE,
         V_IP, V_DEPTYPE, V_DEPFUNCTION, ORGANIZATION, V_PORT)
      select d.UUID, d.REMARK, d.OCA, d.LASTMODIFYTIME, d.V_DEPSTATE,
         d.V_IP, d.V_DEPTYPE, d.V_DEPFUNCTION, d.ORGANIZATION, d.V_PORT
      from department d,Rborganization o
      where d.organization = o.uuid and o.code = vStoreCode;

      commit;
      return(0);
    exception
      when others then
      begin
        rollback;
        poErrMsg := '错误号:' || SQLCODE || ',错误信息:' || SQLERRM;
        return(1);
      end;
    end;
  end;

begin
  -- Initialization
  null;
end POS_STORE_CARD;
----------end