#!/usr/bin/python
#coding=utf-8

'''
	对于数据库已经存在的表结构，可以直接auto_load加载
'''

from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.orm import sessionmaker,mapper

engine = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',coerce_to_unicode=True)
metadata = MetaData(bind=engine)
Session_class = sessionmaker(bind=engine)
##如果表已经存在，设置属性autoload=True
# users = Table('test_wang2',metadata,autoload=True)
address =  Table('test_wang3',metadata,autoload=True)

class User(object):
    pass  ##如果类不重写构造函数，映射后就不能创建对象进行插入操作，构造函数参照如下
    # def __init__(self,id,name,password):
    #     self.id = id
    #     self.name = name
    #     self.password = password

class Addr(object):
    pass


#metadata.create_all(bind=engine)
# mapper(User,users)
# mapper(Addr,address)
# session = Session_class() ##会话类实例


#插入数据（在重写了构造函数后）
# u = User(9,'0009','test')
# session.add(u)
# session.commit()

# 查询操作
# for instance in session.query(User):
#     print instance.id,instance.name
# for user_id,user_name in session.query(User.id,User.name):
#     print user_id,user_name
#数组切片访问
# for u in session.query(User).order_by(User.id)[1:3]:
#     print u.id,u.name
#filter_by()筛选
# for name in session.query(User.name).filter_by(id = 2):
#     print name
# # filter()筛选,注意和filter_by()的区别
# for name in session.query(User.name).filter(User.id == 2):
#     print name
# 多条件查询，可重复使用filter()或者filter_by()
# for name in session.query(User.name).filter(User.id == 2).filter(User.name == '0002'):
#     print name
# 常用操作符
# query = session.query(User.name) #查询返回后是对象的某个字段
# query_U = session.query(User) #查询后返回的是一个对象
# 等于,不等于，like
# print query.filter(User.name == '0002').first()
# print query.filter(User.name != '0002').first()
# print query.filter(User.name.like('0002%')).first()
# IN,NOT IN,IS NULL,IS NOT NULL
# print query.filter(User.name.in_(['0002','0007'])).first()
# print query.filter(~User.name.in_(['0002','0007'])).first()
# print query.filter(User.name == None).first()
# print query.filter(User.name.is_(None)).first()
# print query.filter(User.name != None).first()
# print query.filter(User.name.isnot(None)).first()
# AND
# use and_()
# print query.filter(and_(User.name == '0002', User.id == 2)).first()
# # or send multiple expressions to .filter()
# print query.filter(User.name == '0002', User.id == 2).first()
# # or chain multiple filter()/filter_by() calls
# print query.filter(User.name == '0002').filter(User.id == 2).first()
# # OR
# print query.filter(or_(User.name == '0002', User.id == 2)).first()
# NOT
#print query.filter(not_(User.name == '0002')).first()
# all()/first()/one()
# all()返回的是一个列表,first()返回第一条，one()返回一条，如果有多天则报错
# print ("all(): ",query_U.filter(not_(User.name == '0002')).all())
# print ("first(): ",query_U.filter(not_(User.name == '0002')).first())
# print ("one(): ",query_U.filter(User.name == '0002').one())
# 结合test()方法，实现SQL化查询，不建议使用，比如
# print query.filter(text("id != 2")).order_by(text("id")).all()
# print query.filter(text("id != :id")).params(id = 2).order_by(text("id")).all()
# print query.from_statement(text("SELECT * FROM test_wang2 where id !=:id")).params(id = 2).all()

# 统计
# print query.filter(text("id != 2")).count()
# 关联查询
# for u, a in session.query(User, Addr).filter(User.id==Addr.user_id).filter(Addr.email_address=='wang@1122').all():
#     print (u.name,a.email_address)
# join
# for u in session.query(User).join(Addr,User.id==Addr.user_id).filter(Addr.email_address=='wang@1122').all():
#     print (u.user_id)


# 更新
# name_1 = query_U.filter(User.name == '0002').first()
# name_1.name = '0002_modify'
# session.commit()

# 删除
# name_1 = query_U.filter(User.name == '0007').first()
# session.delete(name_1)
# session.commit()
# drop表
metadata.drop_all(bind=engine,tables=[address])