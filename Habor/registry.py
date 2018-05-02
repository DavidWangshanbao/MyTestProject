#!/usr/bin/python
# -*- coding:UTF-8 -*-
from __future__ import unicode_literals, print_function
import requests


image='jposbo'
BASE_URL = 'https://dockerhub.hd123.com'
auth = ('lijian', 'ooVGfdtr05WniQS8')
from urllib import quote_plus

url = '{}/v2/{}/tags/list'.format(BASE_URL, quote_plus(image))
res = requests.get(url, auth=auth,timeout=10)
res_json = res.json()
print(res.headers)
print(len(res_json.get('tags')))
print(res_json.get('tags')[0])