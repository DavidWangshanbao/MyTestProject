# -*- coding: UTF-8 -*-

## ====================================
##  HTTP请求
## ====================================
HOST = "https://pay-test.qianfan123.com"
HEADERS = {
        'Accept': 'application/json;charset=utf-8',
        'content-type': 'application/json;charset=utf-8',
    }

HTTP_REQUEST_TIMEOUT = 5


## ====================================
##  datatime format
## ====================================
YYYYMMDDHHMMSS="%Y-%m-%d %H:%M:%S"
YYYYmmdd="%Y-%m-%d"


from io import open
import os
import time
import demjson
import codecs


def ts():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def json_encode(obj):
    return demjson.encode(obj, compactly=False) \
        .replace('\\n', '\n') \
        .replace('\\t', '\t') \
        .replace('\\\\', '\\')


def print_file(fileName):
    print(''.ljust(40, '-'))
    print('File: ' + fileName)
    print(''.ljust(40, '-'))
    file = open(fileName, "r", encoding="utf-8")
    print(file.read())
    file.close()

