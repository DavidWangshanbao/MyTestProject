#!/usr/bin/python
#coding=utf-8

'''
	多个表对象进行relationship关联，从而实现关联查询
'''

from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',coerce_to_unicode=True)
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


class Addr(Base):
    __tablename__='test_wang3'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30))
    user_id = Column(Integer, ForeignKey('test_wang2.id'))
    user_map = relationship("User",back_populates="test_table3")
    #back_populates就是一个类和另一个类联系时的名称，可以实现双向互补

User.test_table3 = relationship("Addr", order_by=Addr.id, back_populates="user_map")
#Addr.user_map 就相当于 User类的一个对象, 另一方面 User.test_wang3 相当于Addr对象的一个列表.


class Addr2(Base):
    __tablename__='test_wang4'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30))
    user_id = Column(Integer, ForeignKey('test_wang2.id'))
    user_map2 = relationship("User", backref="my_addr")
#backref参数相当于给链接的名字，但不是双向的，注意和back_populates选项的区别，back_populates是backref升级版

Base.metadata.create_all(bind=engine)
session = Session_class() ##会话类实例

# u1 = User(id =2,name='0002',password='12345')
# u1.test_wang3=[Addr(id = 1122,email_address='wang@1122',user_id=2)]  #注意是列表
# session.add(u1)


# u1 = User(id =1,name='0001',password='12345')
# a1 = Addr(id = 1234,email_address='wang@ssa',user_id=1)
# a2 = Addr2(id = 1234,email_address='wang@ssa',user_id=1)
# session.add_all([u1,a1,a2])

#session.commit()
# jack1 = session.query(User).filter_by(name='0002').first().test_table3
# jack2 = session.query(Addr).filter_by(id=1122).first().user_map
# jack3 = session.query(User).filter_by(name='0001').first().my_addr
# #以上关联的主键对应的其他表的外键有值才能有数据，不然返回的是空列表[]
# print jack1  #返回的是Addr类型
# print jack2   #返回的是User类型
# print jack3   #返回的是Addr类型

