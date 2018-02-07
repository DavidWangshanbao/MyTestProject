# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/v2/shop"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create(session, baseurl, body):
    """
    新增保存门店信息
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "create"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get(session, baseurl, shop):
    """
    修根据uuid获取门店
    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def getByUser(session, baseurl, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/ByUser"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def invited_list(session, baseurl, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "invited/list"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def list(session, baseurl, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "list"
    return curl(url, session).headers(headers).params(id=id).perform()


def modify(session, baseurl, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "modify"
    return curl(url, session).method('post').headers(headers).body(body).perform()
