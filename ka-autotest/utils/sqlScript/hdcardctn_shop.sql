----卡中心门店商品资料
-------start
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
/
--------------end
--------------start
create or replace package hdpos4tohdcard is
  procedure goodssyn;
end  hdpos4tohdcard;
/
--------------end
--------------start
create or replace package body hdpos4tohdcard is
procedure goodssyn is
  vcount int;
  cursor c is
  select g.name       name,
         g.code       code,
         gdinput.code inputcode,
         g.spec       spec,
         g.gid        gid,
         g.qpc        qpc,
         g.rtlprc     rtlprc,
         g.munit      munit,
         br.code      brandcode,
         br.name      brandname,
         st.scode   categoryCode,
         st.sname      categoryname
  from goods@link_pos4   g left join gdinput@link_pos4 gdinput on g.gid = gdinput.gid
  left join sortname@link_pos4 st on g.sort=st.scode and st.lvl=3
  left join brand@link_pos4 br on g.brand=br.code
 where  gdinput.lstupdtime > sysdate - 1;
begin
  for r in c loop
    select count(1)into vcount from cardgoodsinputcode where r.inputcode=inputcode;
    if vcount=0 then
      insert into cardgoodsinputcode(uuid,goodsname,goodscode,spec,gdgid,qpc,goodsprice,inputcode,munit,brandcode,brandname,categoryCode,categoryname)
      values (sys_guid(),r.name,r.code,r.spec,r.gid,r.qpc,r.rtlprc,r.inputcode,r.munit,r.brandcode,r.brandname,r.categoryCode,r.categoryname);
      else
        update cardgoodsinputcode set goodsname=r.name,goodscode=r.code,spec=r.spec,qpc=r.qpc,goodsprice=r.rtlprc,inputcode=r.inputcode,munit=r.munit,
        brandcode=r.brandcode,brandname=r.brandname,categoryCode=r.categoryCode,categoryname=r.categoryCode where inputcode=r.inputcode;
    end if;
  end loop;
  commit;
end;
end hdpos4tohdcard;
/
--------------end
--------------start
declare
  vjobno number;
begin
  sys.dbms_job.submit(job => vjobno,
                      what => 'begin
  hdpos4tohdcard.goodssyn;
end;',
                      next_date => to_date('current_system_datetime', 'dd-mm-yyyy hh24:mi:ss'),
                      interval => 'sysdate+5/1440');
  commit;
end;
--------------end
