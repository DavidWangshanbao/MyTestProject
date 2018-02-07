#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
# 打开数据库连接
db = pymysql.connect(host= "172.17.12.23",port = 3306,user = "root",passwd = "headingjpos",db = "test" )
# 获取游标
cursor = db.cursor()
# 执行SQL
sql = "select * from test_wang"
cursor.execute(sql)
# 获取数据
data = cursor.fetchone()
print(data)
# 关闭游标
cursor.close()
# 关闭连接
db.close()