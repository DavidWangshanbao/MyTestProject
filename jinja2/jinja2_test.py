#!/usr/bin/python
#coding=utf-8

from jinja2 import Template

def readFromFile(filename):
    with open(filename,"r") as fp:
        read_buf = fp.read()

    return  read_buf


def gen_template():
    t = Template(readFromFile("test.j2"))
    res = t.render(name = "David wang",info = {"age":24,"email":"www.wang"},place = ("shanghai","luan"),books = ["python","java",'shell',"C++"])
    print res

    return  res

if __name__ == "__main__":
    gen_template()




