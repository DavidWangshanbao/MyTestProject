#!/usr/bin/python
# -*- coding:UTF-8 -*-
from __future__ import unicode_literals, print_function
from docker.registryapi import RegistryApi
import humanfriendly
import arrow
import os
import re


def time_format(time_str):
    dt = arrow.get(time_str)
    dt_formate = dt.strftime("%Y/%m/%d %H:%M:%S")
    return  dt_formate

def get_size(res_layers):
    ##res_layers = res["layers"]
    size_list = []
    for i in res_layers:
        size_list.append(i["size"])
    sum_size = sum(size_list)
    return humanfriendly.format_size(sum_size,binary=True)

def get_time(res_configContent):
    create_time = res_configContent["created"]
    return time_format(create_time)

def cmp_tags(x,y):
    date_x = re.findall(r".*_(\d+).*",x)
    date_y = re.findall(r".*_(\d+).*",y)
    if date_x[0] > date_y[0]:
        return  1
    elif date_x[0]  < date_y[0]:
        return -1
    else:
        return  0


def gen_jposbo_wiki(number=100):
    #pattern = r"2018041"
    current_path = os.path.abspath('.')
    jposbo_file_path = os.path.join(current_path,"docs/jposbo/jposbo.md")
    url = 'https://harborka.qianfan123.com'
    username= 'admin'
    password='XJOvN1GhQQk8eyUc'
    registry = RegistryApi(username, password, url)
    repository = "jposbo/jposbo"
    res =registry.getTagList(repository)
    tags=res.get('tags')
    #filtered_tags=filter(lambda tag :re.search(pattern,tag) ,tags)
    sort_tags = sorted(tags,cmp=cmp_tags,reverse=True)
    filtered_tags = sort_tags[0:number]
    # for i in tags:
    #     is_match = re.search(pattern,i)
    #     if not is_match:
    #         tags.remove(i)
    with open(jposbo_file_path, "a") as new_file:
        for tag in filtered_tags:
            image_tag_info = registry.getManifestWithConf(repository,tag)
            size = get_size(image_tag_info["layers"])
            time = get_time(image_tag_info["configContent"])
            new_file.write("| {} | {} | {} | \n".format(tag,size,time))



if __name__ == "__main__":
    gen_jposbo_wiki()