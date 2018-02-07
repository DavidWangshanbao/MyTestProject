#!/usr/bin/python
#coding=utf-8

list = [1,2,3]
tuple = (4,5,6)
dict  = {"name":"wang","age":24}


def add_fn(a, b, c):
    return a + b + c

def add_dict(name,age):
    res = "my name is %s,age %d" % (name,age)
    return res


sum = add_fn(*list)
sum2 = add_fn(*tuple)
sum3 = add_dict(**dict)
print("列表参数解包： %s" %  sum)
print("元组参数解包： %s" %  sum2)
print("字典参数解包： %s" %  sum3)