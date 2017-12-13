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
    if os.path.exists("replace.sql"):
        os.remove("replace.sql")

    fo = open("replace.sql","a+")
    for rx in range(1,sh.nrows):
        valus = sh.row_values(rx)
        line_num=valus[0]
        order_id=valus[1]
        new_skuid=valus[2]
        old_skuid=valus[4]
        sku_name=valus[6]
        ###修复错误数据
        sql1="update `so_order_item` set `front_sku_id` = '" + new_skuid + "'," + "`sku_id` = '" + new_skuid + "' where order_uuid = (select uuid from `so_order` where `order_id` = '" +  order_id + "') and `front_sku_id`= '" + old_skuid + "';\n"
        ###更新索引
        sql2="""insert into so_event(uuid, tenant_id, retries, event_type, handlers, created, payload)  select uuid(),`tenant_id`,0,'com.hd123.soms.core.order.event.OrderModified','index',now(),concat('{"tenantId":"',tenant_id,'","orderId":"', order_id, '","logActions":"cancel,op_shipping,deliver_signed,deliver_shipped,deliver_refused,deliver_redeliver,op_handover"}') from so_order where order_id = '""" + order_id + "';\n"
        fo.write(sql1)
        fo.write(sql2)

    fo.close()
    print("转换完成，请查看replace.sql文件")
    return 0


readxlsx()

