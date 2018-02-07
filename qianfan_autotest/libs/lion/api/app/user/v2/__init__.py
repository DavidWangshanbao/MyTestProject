# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/v2/user"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def save(session,baseurl,body):
    """
    修改保存用户信息
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl= _get_prefix(baseurl)
    url = _baseurl  + 'save'
    return curl(url,session).method('post').headers(headers).body(body).perform()