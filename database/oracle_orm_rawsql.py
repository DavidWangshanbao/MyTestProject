#!/usr/bin/python
#coding=utf-8

'''
    结合execute,使用原生的sql语句
'''

from sqlalchemy import *
import  os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

oracle_db = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',coerce_to_unicode=True)
#推荐使用text函数

def query():
    result = oracle_db.execute(text('select * from test_wang where code > :code'),{'code': '0003'})
    for rows in result:
        #print dict(rows)
        print rows['code'],rows['name'] # rows['code'] = row[0] = rows.code

def insert():
    conn = oracle_db.connect()
    conn.begin()
    try:
        result = oracle_db.execute(text('delete test_wang where code = :code'),{'code': '0010'})
        result = oracle_db.execute(text('insert into test_wang values(:code,:name)'), {'code': '0010', 'name':u'中文测试哈哈'})
    except Exception, e:
        print(e)

    conn.close()

insert()
query()
