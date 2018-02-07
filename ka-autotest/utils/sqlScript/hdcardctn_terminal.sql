------卡中心终端同步

-------------start
create table IMPDATARESULT
(
  cls     VARCHAR2(100) not null,
  uuid    VARCHAR2(100) default '-' not null,
  ret     INTEGER default 0,
  content VARCHAR2(1000),
  fildate DATE default SYSDATE not null
)
;
/
-------------end
-------------start
create or replace package hdpos4tohdcard_terminalsyn is
  -- Purpose : 该包用于向 HDCARD 导入终端数据,部署在卡中心的普通库
  function ImpTerminal(poErrMsg out varchar2) return number;
end hdpos4tohdcard_terminalsyn;
/
-------------end
-------------start

create or replace package body hdpos4tohdcard_terminalsyn is
  procedure AddLog(
    piCls in varchar2,
    piUUID in varchar2,
    piResult in integer,
    piContent in varchar2) is
  begin
    insert into ImpDataResult(Cls, Ret, Content, UUID)
    values(piCls, piResult, piContent, piUUID);
    commit;
  end;

  ---终端插入
  function TerminalInsert(
    piTerminalId in Terminal.v_Id%type,
    piServerId in Terminal.v_id%type,
    piStoreCode in Terminal.Storecode%type,
    piExpireDate in Terminal.d_Expiredate%type,
    poErrMsg out varchar2) return number
  is
    vTerminalId   Terminal.v_Id%type; --终端代码
    vServerId     Terminal.v_Id%type; --服务端代码
    vStoreCode    Terminal.Storecode%type; --所属门店代码
    vExpireDate   Terminal.d_Expiredate%type; --到效期
    vTerminalUuid Terminal.Uuid%type;
    vServerUuid Terminal.Uuid%type;

    vStoreName    Terminal.Storename%type;
    vStoreUuid    Terminal.Storeuuid%type; 
    vStarterUuid  Terminal.Starteruuid%type; --组织UUID
    vStarterName  Terminal.Startername%type; --组织名称
    vStarterCode  Terminal.Startercode%type; --组织代码
    vHasServerId  int;
    vCenterCode   varchar2(100);
  begin
    begin
      vTerminalId   := piTerminalId;
      vServerId     := piServerId;
      vStoreCode    := piStoreCode;
      vExpireDate   := piExpireDate;
      vTerminalUuid := sys_guid();
      vServerUuid   := sys_guid();
      vCenterCode   := '8888'; --需要根据现场部署情况修改

      select uuid, name into vStoreUuid, vStoreName from Rborganization where code = vStoreCode;

      select uuid, name, code into vStarterUuid, vStarterName, vStarterCode
        from rborganization where code = vCenterCode;

      if (vTerminalId = vServerId) then
        insert into Terminal(UUID, REMARK, OCA, V_ID,TERMINALNAME,I_SATUS,
          I_TYPE, D_EXPIREDATE, V_REGISTNUM, V_SERVERID, I_EXPIREPROMPTINDAYS,
          I_SYNINTERINMINS, I_UPLOADINTERINSECS, I_FILEAPPENDERMAXSIZE, I_FILEAPPENDERKEEPDAYS, I_FILEAPPENDERLEVEL ,
          I_TCPSERVERTHREADS, I_SESSIONLIFEINMINS, I_LOGININTERVALINSECS, I_CALLTIMEOUTINMILLISECONDS, I_EXCLUDATADOWNLOADINMINS,
          I_SHARDDATADOWNLOADINMINS, I_CHECKVERSIONINHOURS, STORENAME, STOREUUID, STORECODE,
          I_SERVERTYPE, SPOSOFFLINE, LIMITFUNCTION, RECEIPTCOPIES, ENABLEUPGRADE,
          STARTERUUID, STARTERNAME, STARTERCODE, LASTMODIFYTIME, CREATEOPERNAME, CREATEOPERCODE, CREATETIME, LASTMODIFYOPERNAME, LASTMODIFYOPERCODE)
        values(vTerminalUuid, 'POS4数据导入', '0', vTerminalId,vTerminalId,'UNREGISTERED',
          'BOTH', vExpireDate, vTerminalId, vTerminalId, '10',
          '10', '10', '2', '7', 'DEBUG',
          '10', '480', '10', '60000', '60',
          '720', '1', vStoreName, vStoreUuid, vStoreCode,
          'SPOS', '1', '0000000000', '1', '1',
          vStarterUuid, vStarterName, vStarterCode, SysDate, '初始系统导入', 'admin', sysdate, '初始系统导入', 'admin');
      end if;

      if (vTerminalId <> vServerId) then
       select count(uuid) into vHasServerId from Terminal where v_id = vServerId;
       if(vHasServerId = 0) then
         insert into Terminal(UUID, REMARK, OCA, V_ID,TERMINALNAME,I_SATUS,
          I_TYPE,D_EXPIREDATE ,V_REGISTNUM ,V_SERVERID ,I_EXPIREPROMPTINDAYS ,
          I_SYNINTERINMINS,I_UPLOADINTERINSECS ,I_FILEAPPENDERMAXSIZE ,I_FILEAPPENDERKEEPDAYS ,I_FILEAPPENDERLEVEL ,
          I_TCPSERVERTHREADS, I_SESSIONLIFEINMINS, I_LOGININTERVALINSECS, I_CALLTIMEOUTINMILLISECONDS, I_EXCLUDATADOWNLOADINMINS,
          I_SHARDDATADOWNLOADINMINS, I_CHECKVERSIONINHOURS, STORENAME, STOREUUID, STORECODE,
          I_SERVERTYPE, SPOSOFFLINE, LIMITFUNCTION, RECEIPTCOPIES, ENABLEUPGRADE,
          STARTERUUID, STARTERNAME, STARTERCODE,LASTMODIFYTIME, CREATEOPERNAME, CREATEOPERCODE, CREATETIME, LASTMODIFYOPERNAME, LASTMODIFYOPERCODE)
        values(vServerUuid, '数据导入', '0', vServerId,vTerminalId, 'UNREGISTERED',
          'SERVER', vExpireDate, vServerId, vServerId, '7',
          '10', '10', '2', '7', 'DEBUG',
          '10', '480', '10', '15000', '60',
          '720', '1', vStoreName, vStoreUuid, vStoreCode,
          'SPOS', '1', '0000000000', '1', '1',
          vStarterUuid, vStarterName, vStarterCode,sysdate, '系统导入', 'admin', sysdate, '系统导入', 'admin');
       end if;

       insert into Terminal(UUID, REMARK, OCA, V_ID,TERMINALNAME,I_SATUS,
          I_TYPE,D_EXPIREDATE ,V_REGISTNUM ,V_SERVERID ,I_EXPIREPROMPTINDAYS ,
          I_SYNINTERINMINS,I_UPLOADINTERINSECS ,I_FILEAPPENDERMAXSIZE ,I_FILEAPPENDERKEEPDAYS ,I_FILEAPPENDERLEVEL ,
          I_TCPSERVERTHREADS, I_SESSIONLIFEINMINS, I_LOGININTERVALINSECS, I_CALLTIMEOUTINMILLISECONDS, I_EXCLUDATADOWNLOADINMINS,
          I_SHARDDATADOWNLOADINMINS, I_CHECKVERSIONINHOURS, STORENAME, STOREUUID, STORECODE,
          I_SERVERTYPE, SPOSOFFLINE, LIMITFUNCTION, RECEIPTCOPIES, ENABLEUPGRADE,
          STARTERUUID, STARTERNAME, STARTERCODE,LASTMODIFYTIME, CREATEOPERNAME, CREATEOPERCODE, CREATETIME, LASTMODIFYOPERNAME, LASTMODIFYOPERCODE)
        values(vTerminalUuid, '数据导入', '0', vTerminalId,vTerminalId, 'UNREGISTERED',
          'TERMINAL', vExpireDate, vTerminalId, vServerId, '10',
          '10', '10', '2', '7', 'DEBUG',
          '10', '480', '10', '15000', '60',
          '720', '1', vStoreName, vStoreUuid, vStoreCode,
          'SPOS', '1', '0000000000', '1', '1',
          vStarterUuid, vStarterName, vStarterCode,sysdate, '系统导入', 'admin', sysdate, '系统导入', 'admin');
      end if;
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


  function ImpTerminal(poErrMsg out varchar2) return number
  is
    vRet int;
    vHasTerminalId int;

    cursor c_TerminalId is
      select w.no terminalId,
             w.no serverId,
             s.code storeCode,
             to_date('2099-01-01', 'yyyy-mm-dd') expireDate
        from store@link_pos4 s, WORKSTATION@link_pos4 w
       where w.STOREGID = s.gid
         and w.style = 0
         and not exists
       (select 1 from terminal t where t.v_id = w.no);

  begin
    for curDtl in c_TerminalId loop
      select count(uuid) into vHasTerminalId
      from Terminal
      where v_id = curDtl.terminalId;

      if (vHasTerminalId = 0) then
        vRet := TerminalInsert(curDtl.terminalId, curDtl.serverId, curDtl.storeCode, curDtl.expireDate, poErrMsg);

        if (nvl(vRet,'0') = '0') then
          ADDLOG('TERMINAL', '终端：'||curDtl.terminalId ||'; 所属服务器：'|| curDtl.serverId, vRet, '终端资料导入HDCARD成功');
        elsif (nvl(vRet,'1') = '1') then
          ADDLOG('TERMINAL', '终端：'||curDtl.terminalId ||'; 所属服务器：'|| curDtl.serverId, vRet, '终端资料导入HDCARD失败 ' || poErrMsg);
        end if;
      end if;
      if (vHasTerminalId <> 0) then
        ADDLOG('TERMINAL', '终端：'||curDtl.terminalId ||'; 所属服务器：'|| curDtl.serverId, 1, '终端资料在HDCARD数据库中已经存在');
      end if;
    end loop;
    return(0);
  end;

begin
  -- Initialization
  null;
end hdpos4tohdcard_terminalsyn;

/
-------------end
-------------start
declare
  vjobno number;
begin
  sys.dbms_job.submit(job =>  vjobno,
                      what => 'declare
vret integer;
poerrmsg varchar2(255);
begin
vret:=hdpos4tohdcard_terminalsyn.ImpTerminal(poErrMsg);
end;',
                      next_date => to_date('current_system_datetime', 'dd-mm-yyyy hh24:mi:ss'),
                      interval => 'sysdate+5/1440');
  commit;
end;