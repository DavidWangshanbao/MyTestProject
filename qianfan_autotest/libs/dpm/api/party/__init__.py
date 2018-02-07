# coding=utf-8
"""
分润方服务
"""
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "party"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def post(session, baseurl, string, party):
    """
    新增或修改保存。根据坐标判断是否已经存在，决定新增或修改。
    忽略版本检查。
    :param session:
    :param baseurl:
    :param string:
    :param party:
    :return:
    """
    url = _get_prefix(baseurl)
    return curl(url, session).method('post').headers(string=string).body(party).perform()


def get(session, baseurl, uuid):
    url = _get_prefix(baseurl)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getByCoordinate(session, baseurl, uuid):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getByCoordinate'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def fetchChainDealer(session, baseurl, fetchParts, qd):
    """
    查询联锁总部
    :param session:
    :param baseurl:
    :param fetchParts:
    :param qd:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'fetchChainDealer'
    return curl(url, session).method('post').headers(headers).params(fetchParts=fetchParts).body(qd).perform()


def queryParty(session, baseurl, fetchParts, qd):
    """
    查询分润方信息
    :param session:
    :param baseurl:
    :param fetchParts:
    :param qd:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'queryParty'
    return curl(url, session).method('post').headers(headers).params(fetchParts=fetchParts).body(qd).perform()


def queryShop(session, baseurl, fetchParts, qd):
    """
    查询分润方信息
    :param session:
    :param baseurl:
    :param fetchParts:
    :param qd:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'queryShop'
    return curl(url, session).method('post').headers(headers).params(fetchParts=fetchParts).body(qd).perform()
