#!/usr/bin/python
#coding=utf-8

def doub(x):
    if x >= 0:
        return True
    else:
        return False





def test():
    mylist = [1,-2,3,-4]
    mylist2 = filter(doub,mylist)
    print mylist2



test()