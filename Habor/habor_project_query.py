#!/usr/bin/python
# -*- coding:UTF-8 -*-
from __future__ import unicode_literals, print_function
from gen_wiki import *
import re
import argparse
import arrow
from docker.harborclient import HarborClient
import humanfriendly
from markdowntohtml.MarkdownPreview import MarkdownCompiler, save_utf8
import codecs

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

allfile = []



def time_format(time_str):
    dt = arrow.get(time_str)
    dt_formate = dt.strftime("%Y/%m/%d %H:%M:%S")
    return  dt_formate

def readFromFile(filename, encoding=None):
    result = None
    encoding = encoding or 'utf-8'
    with codecs.open(filename, encoding=encoding) as fp:
        result = fp.read()
    return result

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass

def md_to_html(project_name_list):
    for project_name in project_name_list:
        docs_ads_path = os.path.abspath('./docs')
        htmlfile_abs_path = os.path.abspath('./htmlfile')
        dir_path = os.path.join(docs_ads_path,project_name)
        html_dir_path = os.path.join(htmlfile_abs_path,project_name)
        file_list = os.listdir(dir_path)
        for file_name in file_list:
            compiler = MarkdownCompiler()
            file_path = os.path.join(dir_path,file_name)
            html, body = compiler.run(None, True, preview=False, contents=readFromFile(file_path))
            mkdir(html_dir_path)
            save_utf8("{}/{}.html".format(html_dir_path,file_name), html)


def get_projectid_byname(client, project_name):
    if not client.check_project_exist(project_name):
        raise ValueError("project {} doese not exist".format(project_name))
    projects = client.get_projects()
    filtered = filter(lambda x: x.get('name') == project_name, projects)
    return filtered[0].get('project_id')


def dirlist(file_format,path=None):
    if path == None:
        current_path = os.path.abspath('.')
    else:
        current_path = path
    filelist = os.listdir(current_path)
    for filename in filelist:
        filepath = os.path.join(current_path, filename)
        if os.path.isdir(filepath):
            dirlist("md",filepath)
        elif os.path.isfile(filepath) and re.search('\.'+file_format,filename) != None:
            allfile.append(filepath)
        else:
            continue
    return allfile


def init_sep_file(filepath,filetype):
    current_path = os.path.abspath('.')
    index_file = current_path + '/docs/index.md'
    if filepath == index_file:
        with open(filepath,"w") as new_file:
            new_file.write("")
            if filetype == "md":
                new_file.write("| 项目名称 | 镜像仓库数 | 创建时间 |" + "\n")
                new_file.write("| -------- | ---- | -------- |" + "\n")
            else:
                new_file.write("|| 项目名称 || 镜像仓库数 || 创建时间 ||" + "\n")
    else:
        with open(filepath,"w") as new_file:
            new_file.write("")
            if filetype == "md":
                new_file.write("| 名称 | 标签数 | 下载数 |"+"\n")
                new_file.write("| -------- | ---- | -------- |"+"\n")
            else:
                new_file.write("|| 名称 || 标签数 || 下载数 ||" + "\n")



def init_all_mdfile(filetype):
    current_path = os.path.abspath('.')
    file_list = dirlist("md")
    for i in file_list:
        with open(i, 'w') as new_file:
            new_file.write("")
            if filetype == "md":
                new_file.write("| 名称 | 标签数 | 下载数 |"+"\n")
                new_file.write("| -------- | ---- | -------- |"+"\n")
            else:
                new_file.write("|| 名称 || 标签数 || 下载数 ||" + "\n")
    index_file = current_path + '/docs/index.md'
    with open(index_file, 'w') as new_file:
        if filetype == "md":
            new_file.write("| 项目名称 | 镜像仓库数 | 创建时间 |"+"\n")
            new_file.write("| -------- | ---- | -------- |"+"\n")
        else:
            new_file.write("|| 项目名称 || 镜像仓库数 || 创建时间 ||" + "\n")



def get_allrepositorys(client,all_projects_name):
    all_repositorys_name = []
    for project_name in all_projects_name:
        project_id = get_projectid_byname(client, project_name)
        repo_name = client.get_repositories(project_id)
        for i in repo_name:
            all_repositorys_name.append({"name":i['name'],"tags_count":i['tags_count'],"pull_count":i['pull_count']})
    return all_repositorys_name



def wrt_index_file(client):
    #写入index.md
    current_path = os.path.abspath('.')
    index_file = current_path + '/docs/index.md'
    #获取所有项目信息
    project_info = client.get_projects()
    if not os.path.exists(index_file):
        init_sep_file(index_file,"")
    with open(index_file, 'a') as new_file:
        for i in project_info:
            new_file.write("| {} | {} | {} | \n".format(i["name"],i["repo_count"],time_format(i["creation_time"])))

def wrt_tags_file(client,reponame_list):
    current_path = os.path.abspath('.')
    for repo_info in reponame_list:
        repo_name = repo_info["name"]
        repo_tags_count = repo_info["tags_count"]
        repo_pull_count = repo_info["pull_count"]
        repo1 = repo_name.split('/')[0]
        repo2 = repo_name.split('/')[1]
        repo_name_tags = client.get_repository_tags(repo_name)
        file_rela_path = "docs/{}/{}.md".format(repo1,repo2)
        dir_real_path = "docs/{}".format(repo1)
        dir_path = os.path.join(current_path,dir_real_path)
        file_path = os.path.join(current_path, file_rela_path)
        print("{}文件生成成功".format(file_path))

        # 自动创建项目文件夹
        mkdir(dir_path)
        #判断如果文件不存在，初始化指定文件
        if not os.path.exists(file_path):
            init_sep_file(file_path,"cus")
        with open(file_path,'a') as new_file:
            new_file.write("| {} | {} | {} | \n".format(repo_name,repo_tags_count,repo_pull_count))
            new_file.write("| 标签 | 大小 | 创建时间 |"+"\n")
            for i in sorted(repo_name_tags,key=lambda x:x['created'],reverse=True):
                new_file.write("| {} | {} | {} | \n".format(i["name"], humanfriendly.format_size(i["size"]), time_format(i["created"])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-project', dest='project', required=False, default="dts-store", help=u"输入你想要查看的项目名称")
    args = parser.parse_args()
    my_project_list = args.project.split(",")
    exit_code = 0
    try:
        client = HarborClient("harborka.qianfan123.com","admin","XJOvN1GhQQk8eyUc","https")
        client.login()
        init_all_mdfile("nomd")
        wrt_index_file(client)
        repository_list = get_allrepositorys(client,my_project_list)
        #写入镜像标签信息
        wrt_tags_file(client,repository_list)
        #生成指定WIKI页面
        gen_wiki(my_project_list)
        #生成HTML文件
        #md_to_html(project_list)

    except Exception as e:
        exit_code = 1
        print(e)
    finally:
        client.logout()
        exit(exit_code)

if __name__ == '__main__':
    main()