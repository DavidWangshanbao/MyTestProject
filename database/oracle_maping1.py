#!/usr/bin/python
#coding=utf-8

'''
    ORM映射的第一种方式：
    使用declarative_base创建基类，定义新的类，在类中定义映射的表结构，自动关联映射
    构建对象实例时不需要重写构造函数，也可以重写
'''


from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',echo=True,coerce_to_unicode=True)
##生成一个会话类
Session_class = sessionmaker(bind=engine,autocommit=False)
metadata = MetaData(bind=engine)
#获得基类
Base = declarative_base()


class User(Base):
    __tablename__='test_wang2'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    password = Column(String(30))
    #可以写重写构造函数，写了后创建实例对象时可以传递列表参数，而不是字典形式
    # def __init__(self,id,name,password):
    #     self.id = id
    #     self.name = name
    #     self.password = password

##创建表
Base.metadata.create_all(bind=engine)
#u = User(9,'0009','test') #重写构造函数后，可以这么创建对象，不然会报错
# u1 = User(id =7,name='0007',password='12345')
# u2 = User(id =6,name='0006',password='12345')
session = Session_class() ##会话类实例

# session.add(u1)
#session.add_all([u1,u2])
# session.commit()
result = session.query(User).filter(User.id == 7).first()  #返回的是User类的一个对象
print result.name
#修改直接根据对象属性修改
result.name = '0008'
session.commit()
print result.name
