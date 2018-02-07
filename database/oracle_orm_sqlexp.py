#!/usr/bin/python
#coding=utf-8

'''
	使用table对象操作，非ORM模式
'''

from sqlalchemy import *

engine = create_engine('oracle+cx_oracle://hd40:hd40@172.17.11.254:1521/xftest',coerce_to_unicode=True)
metadata = MetaData(bind=engine)
users = Table('test_wang',metadata,autoload = True)      ##因为表test_wang已经存在，只需要使用autoload属性自动加载即可
ids = Table('test_wang2',metadata,autoload = True)
addr = Table('test_wang3',metadata,autoload = True)
# 插入操作table.insert().values(name='foo')
users.insert().values(code='0011',name='test01w').execute()
# sql1 = users.insert().values(code='0011',name='test01w')  ##与上面等价
# engine.execute(sql1)
# 更新操作table.update().where(table.c.id==7).values(name='foo')
users.update().where(users.c.code=='0010').values(name='test_update').execute()
# 删除操作table.delete().where(table.c.id==7)
users.delete().where(users.c.code=='0005').execute()
# 查询操作table.select().where(table.c.id==7)
sql = users.select(and_(users.c.code=='0001',users.c.name=='hello'))
print sql.execute().fetchall()

##扩展，其他查询关键词
# s = users.select(and_(users.c.code=='0001',users.c.name=='hello'))
# s = users.select(or_(users.c.code=='0001',users.c.code=='0002'))
# s = users.select(not_(users.c.code=='0001'))
# s = users.select((users.c.code=='0001') & (users.c.name=='hello'))  #最好添加（），注意优先级
# s = users.select((users.c.code=='0001') | (users.c.code=='0002'))
# s = users.select(~(users.c.code=='0001'))
#
# s = users.select(users.c.code.in_('0001', '0002'))
# s = users.select(~users.c.code.in_('0001', '0002'))
# s = users.select(users.c.name.like('%he%'))
# s = users.select(users.c.code.between('0001','0003'))
# # 使用ORACLE函数func
#s = users.select(func.substr(users.c.name, 1, 2) == 'he')  ##从第一位开始截取，截取2位，原字符'hello'
# # 直接使用select()函数
# s = select([users], users.c.code != '0001')
# s = select([users.c.name], users.c.code != '0001')
# # count()
# s = select([func.count(users.c.code)])
#s = select([func.count("*")], from_obj=[users])
# 多表关联查询
# s = select([ids, addr], ids.c.id == addr.c.user_id)
# s = select([ids.c.name, addr.c.email_address], ids.c.id == addr.c.user_id)
#print s.execute().fetchall()
