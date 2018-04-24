#!/usr/bin/python
# -*- coding:UTF-8 -*-
from __future__ import unicode_literals, print_function
from confluence.confluence import Confluence
import os
WIKI_USERNAME = 'wangshanbao'
WIKI_PASSWORD = '54325000111'
URL = "http://wiki.app.hd123.cn/wiki"
home_page = "Harbor-KA镜像仓库查看"


def write_Multi_page(space,page,content,parent_name=None):
    try:
        wiki = Confluence(url=URL, username=WIKI_USERNAME, password=WIKI_PASSWORD)
        wiki.write_page(space, page, content,parent_name)
        if  parent_name is None:
            print("{}镜像wiki创建成功".format(page))
        else:
            print("{}镜像wiki创建成功，且父wiki的名称是{}".format(page, parent_name))

    except Exception as e:
        print(e)

def write_index_wiki():
    space = 'QFOPS'
    with open("./docs/index.md","r") as new_file:
        buf = new_file.read()
    write_Multi_page(space,home_page,buf)

def write_project_wiki(pro_list):
    space = 'QFOPS'
    for page in pro_list:
        page = page + "_image"
        content = "h3."+page+u"镜像仓库信息汇总"
        write_Multi_page(space,page,content,home_page)


def write_image_wiki(pro_list):
    space = 'QFOPS'
    current_path = os.path.abspath('./docs')
    for project_page in pro_list:
        image_path = os.path.join(current_path,project_page)
        file_list = os.listdir(image_path)
        for file_fullname in file_list:
            file_name = file_fullname.split(".")[0]
            file_name_path = os.path.join(image_path,file_fullname)
            with open(file_name_path,"r") as new_file:
                buf = new_file.read()
            parent_page_name = project_page + "_image"
            write_Multi_page(space,file_name,buf,parent_page_name)

def gen_wiki(pro_list):
    write_index_wiki()
    write_project_wiki(pro_list)
    write_image_wiki(pro_list)

if __name__ == "__main__":
    pro_list = ["adi","dts-store"]
    gen_wiki(pro_list)


