# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/pos"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, id):
    """
    获取pos机
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(id=id).perform()


def list(session, baseurl, shop):
    """
    获取门店所有的POS机
    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "list"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def save(session, baseurl, body):
    """
    保存POS机信息
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "save"
    return curl(url, session).method('post').headers(headers).body(body).perform()
