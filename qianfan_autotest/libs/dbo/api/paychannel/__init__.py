# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/web/paychannelpayment"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def change_channel(session, baseurl, query, body):
    """
    切换通道
    :param session:
    :param baseurl:
    :param query: 鼎付通商户id
    :param body: cplist
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "changeChannel"
    return curl(url, session).method('post').headers(headers).params(query=query).body(body).perform()


def export(session, baseurl, body):
    """
    商户搜索导出Excel
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "export"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get_pay_channels(session, baseurl):
    """
    获取支付通道
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getPayChannels"
    return curl(url, session).headers(headers).perform()


def query(session, baseurl, body):
    """
    通道列表
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(body).perform()
