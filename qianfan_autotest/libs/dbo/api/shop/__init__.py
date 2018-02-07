# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/web/shop/pay"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def batchUpdate(session, baseurl, serviceProvider, shops):
    """
    批量修改支付服务商信息
    :param session:
    :param baseurl:
    :param serviceProvider:
    :param shops: (BODY)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "batchUpdate"
    return curl(url, session).method('post').headers(headers).params(serviceProvider=serviceProvider).body(
        shops).perform()


def getServiceProvider(session, baseurl):
    """
    获取服务商
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getServiceProvider"
    return curl(url, session).headers(headers).perform()


def query(session, baseurl, query):
    """
    `服务关系`门店查询
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(query).perform()
