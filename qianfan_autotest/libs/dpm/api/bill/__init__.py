# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "bill"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getBillItem(session, baseurl, billUuid, page, pageSize):
    """

    :param session:
    :param baseurl:
    :param billUuid:
    :param page:
    :param pageSize:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getBillItem"
    return curl(url, session).method('post').headers(headers).params(billUuid=billUuid, page=page,
                                                                     pageSize=pageSize).perform()


def manualtrigger(session, baseurl):
    """
    手工触发账单计算
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "manualtrigger"
    return curl(url, session).method('post').headers(headers).perform()


def query(session, baseurl, qd):
    """
    取转账信息
    :param session:
    :param baseurl:
    :param qd:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(qd).perform()
