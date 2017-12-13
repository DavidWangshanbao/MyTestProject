#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals,print_function
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd

def readxlsx():
    filename = sys.argv[1]
    try:
        xlb = xlrd.open_workbook(filename)
    except IOError:
        print("没有 %s 文件" % filename)
        return 1

    sh = xlb.sheet_by_index(0)
    #print(sh.nrows)
    if os.path.exists("push.sql"):
        os.remove("push.sql")

    fo = open("push.sql","a+")
    for rx in range(1,sh.nrows):
        valus = sh.row_values(rx)
        order_id=valus[0]
        ###重新推送
        sql='''insert into nf_notice(uuid, created, creator, modified, modifier, tenant_id, app_id, topic, content, fgroup, business_key, retries, expire_time,is_push,schedule_time) select uuid(), now(), 'admin',now(),'admin',tenant_id,'HDPOS4','order.shipped',concat('{"front_order_id":"', `front_order_id` , '","order_id":"', order_id, '"}'),'order',order_id,0,DATE_ADD(NOW(), INTERVAL 3 DAY),1,1 from so_order where `order_id` = ''' + "'" + order_id + "';\n"
        fo.write(sql)


    fo.close()
    print("转换完成，请查看push.sql文件")
    return 0


readxlsx()

