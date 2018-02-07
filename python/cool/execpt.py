#!/usr/bin/python
#coding=utf-8


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except Exception,e:
        print e

# 调用函数
temp_convert("xyz");