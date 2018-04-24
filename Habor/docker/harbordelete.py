#!/usr/bin/env python
# coding=utf-8
import json

import requests



def get_paginate_query(response):
    if 'Link' in response.headers:
        return response.headers['Link'].split('; ')[0][:-1][1:]
    else:
        return None


command = "REGISTRY_DATA_DIR=/hdapp/harbor/data/registry/docker/registry/v2 python delete_docker_registry_image.py --image {image}:{version}"
url_image = "https://harborhd.qianfan123.com"
url_tag = "https://harborhd.qianfan123.com/v2/{image}/tags/list"
auth = ("admin" , "hoS9sTHXQhpGvwa2")


def main() :
    response = requests.get(url_image + "/v2/_catalog",
                            auth=auth)
    nextQuery = get_paginate_query(response)
    repositories = response.json()["repositories"]

    while nextQuery is not None:
        response = requests.get(url_image + nextQuery,
                                auth=auth)
        repositories.extend(response.json()['repositories'])
        nextQuery = get_paginate_query(response)
    for image in repositories:
        _url_tag = url_tag.format(image=image)
        result_tag = json.loads(requests.get(_url_tag, auth=auth).text)
        if not result_tag.get("tags"):
            print(
            "REGISTRY_DATA_DIR=/hdapp/harbor/data/registry/docker/registry/v2 python delete_docker_registry_image.py --image {image} ".format(
                image=image))
            continue
        for tag in result_tag.get("tags"):
            if not tag.__contains__("SNAPSHOT"):
                continue
            _command = command.format(image=image, version=tag)
            print _command

if __name__ == "__main__" :
    main()