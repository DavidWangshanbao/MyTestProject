#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests

url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
print r.text