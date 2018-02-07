# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "shop"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def put(baseurl, requestId, size):
    url = _get_prefix(baseurl)
    return curl(url).method('put').headers(headers).params(requestId=requestId, size=size).perform()


def getStackIdList(baseurl):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getStackIdList"
    return curl(url).headers(headers).perform()


def gets(baseurl, ids):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "gets"
    return curl(url).method('post').headers(headers).params(ids=ids).perform()


def get(baseurl, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + id
    return curl(url).headers(headers).perform()
