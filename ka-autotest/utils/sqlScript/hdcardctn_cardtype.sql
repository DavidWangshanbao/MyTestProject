--------------卡中心卡类型商品
create or replace procedure card_goods_in(pisort in Varchar2) is
vGoodsGid  INT;
vGdcode    Varchar2(40);
vMunit     Varchar2(40):='个';--单位
vWrh       Varchar2(40):=1000000;--仓库
vVdrGid    Varchar2(40):=1;--供应商
vcode  Varchar2(40);
vcount int;
cursor c is select a.v_code,a.v_name from cardtype a where not exists (select * from cardtypegoods@link_pos4 b where b.cardtype=a.v_code);
begin
   for r in c loop
----设置商品代码，注意根据各项目编码规则自行设置
select  nvl(max(code),substr(pisort,1,2)||'00001')  into vcode from goods@link_pos4 where substr(code,1,2)=substr(pisort,1,2);
vGdcode := vcode+1;
select count(*) into vcount from goods@link_pos4 where code=vgdcode;
if (vcount=0) then
---获取GID
select seq_goods.nextval@link_pos4 into vGoodsGid  from FASYSTEM@LINK_POS4;
----插入商品
Insert into GOODS@LINK_POS4(MODIFIER,MEMO,LIFECYCLE,ALWORD,ALWOUT,ALWALC,
CREATEDATE,SRC,SNDTIME,LSTUPDTIME,ALLOCLIMITQTY,ALLOCSUPPLYQTY,ORDLIMITQTY,
ORDSUPPLYQTY,BACKRATE,PAYMODE,POSGRP,CHKVD,ALCPRC,LWTRTLPRC,DEFINPRC,WHSPRC,
SHORTNAME,ENAME,ESHORTNAME,QPCSTR,VOL,WEIGHT,PURRTN,PTAGSIZE,SALEGRADE,
CHAINGDGID,PROMMERCH,PROMCODE,STORENATURE,PICKSEQ,DISPLAYSTA,DISDATE,REFBIN,
STANREFBIN,PQTY,LADJDATE,ALWWHS,ELIMINATEDATE,ABOLISHDATE,BINDGDGID,BINDRATE,
ALWSORD,CODE3,EQUIP,AREA,MINSHELFCNT,STOREV,DISP,SELLPROP,ISDISP,ICONFILE,
IMAGEFILE,ICONFILEUUID,IMAGEFILEUUID,ICONLSTTIME,IMAGELSTTIME,LTDOPRT,GID,CODE,
NAME,SPEC,SORT,MUNIT,QPC,TM,MANUFACTOR,MCODE,BRAND,ORIGIN,GRADE,PRCTYPE,
VALIDPERIOD,DEP,SLOT,CODE2,GPR,PSR,RTLPRC,INPRC,LSTINPRC,INVPRC,OLDINVPRC,
CNTINPRC,MBRPRC,TAXTYPE,SALETAXTYPE,TAXRATE,SALETAX,PROMOTE,SALE,WRH,ISBIND,GFT,
COSTTYPE,BILLTO,VDRGID,AUTOORD,ALC,LOWINV,HIGHINV,FILLER)
Values ('CARD','分销批量导入',trim('导入期'),1,1,1,
SYSDATE,1000000,TO_Date('1899.12.30 00:00:00','YYYY.MM.DD HH24:MI:SS'),SYSDATE,0,0,0,
0,0,0,'000',0,0,0,0,0,
'','','','1*1','','','R','小',6,
0,0,'','-','F','N', TO_Date('1899.12.30 00:00:00','YYYY.MM.DD HH24:MI:SS'),'',
'1',0,SYSDATE,1,TO_Date('1899.12.30 00:00:00','YYYY.MM.DD HH24:MI:SS'),TO_Date('1899.12.30 00:00:00','YYYY.MM.DD HH24:MI:SS'),0,0,
1,'','-','-',0,'无','','',1,'',
'','','',TO_Date('1899.12.30 00:00:00','YYYY.MM.DD HH24:MI:SS'),TO_Date('1899.12.30 00:00:00','YYYY.MM.DD HH24:MI:SS'),0,vGoodsGid,trim(Vgdcode),
trim(r.v_name),'',trim(pisort),trim(vMUNIT),1,'','','','-','','',0,
0,'-','','',0,'1',0,0,0,0,0,
0,0,0,0,0,0,-1,1,vwrh,0,0,
1,vVdrGid,vVdrGid,0,'统配',0,0,'HDPOS[0]');
-----插入卡类型商品
insert  into cardtypegoods@LINK_POS4(cardtype,gdgid,lstupdtime) values (r.v_code,vGoodsGid,sysdate);
commit;
end if;
end loop;
commit;
end;
----------------------end
----------------------start
declare
  vjobno number;
begin
  sys.dbms_job.submit(job => vjobno,
                      what => 'begin
  card_goods_in(''960101'');
end;',
                      next_date => to_date('current_system_datetime', 'dd-mm-yyyy hh24:mi:ss'),
                      interval => 'sysdate+1');
  commit;
end;
/