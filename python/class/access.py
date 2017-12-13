#!/usr/bin/python
# -*- coding: UTF-8 -*-



class A():
    def test(self):   ##定义了实例方法
        print("normal")
    @classmethod
    def test2(cls):  ##定义了类方法
        print("class")
    @staticmethod
    def test3():##定义了静态方法
        print("static")


demo = A()
demo.test()
A.test(demo)
