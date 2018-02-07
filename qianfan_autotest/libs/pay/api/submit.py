# coding=utf-8
from __future__ import unicode_literals, print_function
import json
import requests
#import codecs
#from utils import baseurl_strip, save_json_file
from const import *

PREFIX = "testbn01/pay/payService/store/0088/submit"


def submit(req):
    """
    被扫提交付款码支付接口
    :param session:
    :param baseurl:
    :param req:string类型
    :return:
    """
    url = HOST + "/" + PREFIX + "/"

    # save_json_file('test.json', json.loads(req, encoding='utf-8'))
    # with codecs.open('test.json', encoding='utf-8') as fp:
    #     return session.post(url, timeout=5, data=fp, headers=headers)
    reqBody=json.dumps(json.loads(req, encoding='utf-8'),ensure_ascii=False).encode('utf-8')
    return requests.post(url, timeout=HTTP_REQUEST_TIMEOUT, data=reqBody,headers=HEADERS)
