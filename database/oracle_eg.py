#!/usr/bin/python
#coding=utf-8

# 引用模块cx_Oracle
import cx_Oracle
#  连接数据库
db=cx_Oracle.connect("hd40/hd40@172.17.11.254:1521/xftest")
# 获取游标cursor
c=db.cursor()
# 使用cursor进行SQL语句
c.execute('select sysdate from dual')
# 取一行数据
result = c.fetchone()
print(result)
# 关闭cursor
c.close()
# 关闭连接
db.close()