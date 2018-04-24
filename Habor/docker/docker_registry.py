# coding=utf-8
"""
follow docker registry api specification
https://github.com/docker/distribution/blob/master/docs/spec/api.md
- catalog: https://dockerhub.1000sails.com/v2/_catalog
- image tag list: https://dockerhub.1000sails.com/v2/{image}/tag/list
"""
from   __future__ import unicode_literals
import re
from pprint import pprint
from bs4 import BeautifulSoup
import requests

# auth = ('dnet', 'ThlVjVebSKB5oTZ5')
# BASE_URL = 'https://dockerhub.1000sails.com'



def find_repositorys(html_content):
    import re
    soup = BeautifulSoup(html_content, 'lxml')
    items = soup.find_all("td")
    for i in items[0::2]:
        x = re.findall('<a href=.*>(.+?)</a>', str(i))[0]
        yield x


def get_all_repos(BASE_URL , auth):
    def get_paginate_query(response):
        if 'Link' in response.headers:
            return response.headers['Link'].split('; ')[0][:-1][1:]
        else:
            return None

    response = requests.get(BASE_URL + "/v2/_catalog", auth=auth)
    nextQuery = get_paginate_query(response)
    repositories = response.json()["repositories"]
    while nextQuery is not None:
        response = requests.get(BASE_URL + nextQuery,
                                auth=auth)
        repositories.extend(response.json()['repositories'])
        nextQuery = get_paginate_query(response)
    return repositories


def get_image_tags(BASE_URL , auth ,image):
    """
     获取指定镜像的tag列表
     获取非snapshot 的镜像 ,SNAPSHOT版本的镜像不需要备份
    :param image: 镜像名称
    :return: [(image,tag1),(image,tag2),...]
    """
    from urllib import quote_plus
    url = '{}/v2/{}/tags/list'.format(BASE_URL, quote_plus(image))
    res = requests.get(url, auth=auth)
    res_json = res.json()
    for tag in res_json.get("tags"):
        if tag.__contains__("SNAPSHOT"):
            continue
        yield image, str(tag)


def get_all_images(BASE_URL , auth):
    repos = get_all_repos(BASE_URL , auth)
    result = []
    for repo in repos:
        for i in (get_image_tags(BASE_URL , auth ,repo)):
            result.append(i)
    return result


if __name__ == "__main__":
    print("==============")
    # auth = ('dnet', 'ThlVjVebSKB5oTZ5')
    # BASE_URL = 'https://dockerhub.1000sails.com'
    # result = get_all_repos(BASE_URL , auth)
    #
    # print(result)
    # print(len(result))
