# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl

PREFIX = "web/web/shop/pay"

headers = {
    'content-type': 'application/json;charset=utf-8'
}


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, body):
    """
    “服务关系”门店的查询
    :param session:
    :param baseurl:
    :param body: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def create(session, baseurl, payJoinCode):
    """
    关联“服务关系”的门店
    :param session:
    :param baseurl:
    :param payJoinCode: String
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'create'
    return curl(url, session).headers(headers).params(payJoinCode=payJoinCode).perform()


def createByShop(session,baseurl,payJoinCode):
    """
    通过门店关联“服务关系”的门店
    :param session:
    :param baseurl:
    :param payJoinCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'createByShop'
    return curl(url,session).headers(headers).params(payJoinCode=payJoinCode).perform()


def createByUser(session,baseurl,payJoinCode):
    """
    通过商户信息关联“服务关系”的门店
    :param session:
    :param baseulr:
    :param payJoinCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'createByUser'
    return curl(url, session).headers(headers).params(payJoinCode=payJoinCode).perform()


def export(session, baseurl, body):
    """
    商户搜索导出Excel
    :param session:
    :param baseurl:
    :param body: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'export'
    return curl(url,session).method('post').headers(headers).body(body).perform()

