# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "sale/guide"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def prepare(session, baseurl, saleTerminal):
    """
    根据算法生成指路牌字符串用于获取产品销售URL
    :param session:
    :param baseurl:
    :param saleTerminal:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'prepare'
    return curl(url, session).method('put').headers(headers).body(saleTerminal).perform()
