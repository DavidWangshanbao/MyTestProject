# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "aeonlife"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def aeonlife_return(session, baseurl, rtn):
    """
    保存退货单,若单号存在则不进行处理
    :param session:
    :param baseurl:
    :param rtn:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "return"
    return curl(url, session).method('post').headers(headers).body(rtn).perform()


def sale(session, baseurl, sale):
    """
    保存销售单,若单号存在则不进行处理
    :param session:
    :param baseurl:
    :param sale:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "sale"
    return curl(url, session).method('post').headers(headers).body(sale).perform()
