# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/shopconfig"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def generateKey(session, baseurl, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "generateKey"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def get(session, baseurl, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def getbyowner(session, baseurl, user, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getbyowner"
    return curl(url, session).headers(headers).params(user=user, mobile=mobile).perform()


def resetkey(session, baseurl, shop, shopId, mobile, authCode, accessKeyId):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "resetkey"
    return curl(url, session).headers(headers).params(shop=shop, shopId=shopId, mobile=mobile, authCode=authCode,
                                                      accessKeyId=accessKeyId).perform()


def save(session, baseurl, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "save"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def update_bykey(session, baseurl, key, shop, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "update/bykey"
    return curl(url, session).method('post').headers(headers).params(key=key, shop=shop).body(body).perform()
