#!/usr/bin/python
#coding=utf-8
"""
    自动映射的方式，缺点：比较慢
"""
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import *


engine = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',coerce_to_unicode=True)
metadata= MetaData()
metadata.reflect(engine,only=['test_wang2'])
Base = automap_base(metadata=metadata)
Base.prepare()
Test = Base.classes.test_wang2
session = Session(engine)
print(session)

# t1= Test(id =9,name='0009',password='12345')
# session.add(t1)
# session.commit()

print (session.query(Test).filter_by(id = 9).first().name)
