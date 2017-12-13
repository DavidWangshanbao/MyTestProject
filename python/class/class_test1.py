#!/usr/bin/python
# -*- coding: UTF-8 -*-

__metaclass__= type  # 使用新式类  3.0后不需此声明


class A():
    u'''哈哈'''
    mysoul = 1
    def __init__(self):
        self.count=1

    def eat(self):
        self.count+=1
        print("eat ok")

    def myprint(self):
        print('A的mypint被调用')



class B(A):
    def __init__(self):
        A.__init__(self)
        #super(B, self).__init__()A
        self.song='lala'


    def myprint(self):
        print('B的mypint被调用')

    def drink(self):
        #print(self.song)
        #A.myprint(self)
        #self.eat()
        #A.eat(self)
        #self.dance()
        B.dance(self)

    def dance():
        print("let's dancing")


if __name__=='__main__':
    demo=B()
    print hasattr(demo,'song')




