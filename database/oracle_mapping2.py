#!/usr/bin/python
#coding=utf-8

'''
    ORM映射的第二种方式：
    table和class分别定义
    新建table或者加载数据库已有表结构
    调用mapper函数进行映射
'''

from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.orm import sessionmaker,mapper

engine = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',coerce_to_unicode=True)
metadata = MetaData(bind=engine)
Session_class = sessionmaker(bind=engine)

users = Table('test_wang2',metadata,
              Column('id',Integer,primary_key=True),
              Column('name',String(50)),
              Column('password',String(30))
              )

##如果表已经存在，设置属性autoload=True
#users = Table('test_wang2',metadata,autoload=True)

class User(object):
    pass
    ##如果类不重写构造函数，映射后就不能创建对象进行插入操作，构造函数参照如下
    # def __init__(self,id,name,password):
    #     self.id = id
    #     self.name = name
    #     self.password = password
metadata.create_all(bind=engine)  #如果是数据库表结构已存在，通过autoload加载，不需要此步骤

mapper(User,users)  #关联映射

session = Session_class() ##会话类实例
print ("Session_class:{}\nsession:{}".format(Session_class,session))
#插入数据（在重写了构造函数后可以进行此操作）
# u = User(9,'0009','test')
# u = User(id =8,name='0008',password='12345')
# session.add(u)
# session.commit()

#查询
query = session.query(User)
print query.all()
print query.all()[0].name  #对象列表
# print query.first().name
# print(query.filter(User.id == 6).first().name)
# query2 = session.query(User.name)
# print(query2.all()) # 每行是个元组
###等等


