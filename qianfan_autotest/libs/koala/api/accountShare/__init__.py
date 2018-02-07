# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/accountShare"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def addShare(session, baseurl, account, destination, s):
    """
    增加设置商户（分享关联关系）
    :param session:
    :param baseurl:
    :param account:
    :param destination:
    :param s:
    :return:
    """
    url = _get_prefix(baseurl) + '_addShare'
    return curl(url, session).method('post').headers(headers).params(**{
        "account": account,
        "destination": destination,
        "string": s
    }).perform()


def addShares(session, baseurl, account, s, destinations):
    """
    批量增加设置商户（分享关联关系）
    :param session:
    :param baseurl:
    :param account:
    :param s:
    :param destinations:
    :return:
    """
    url = _get_prefix(baseurl) + '_addShares'
    return curl(url, session).method('post').headers(headers).params(**{
        "account": account,
        "string": s
    }).body(destinations).perform()


def getShares(session, baseurl, account):
    """
    获取商户
    :param session:
    :param baseurl:
    :param account:
    :return:
    """
    url = _get_prefix(baseurl) + '_getShares'
    return curl(url, session).headers(headers).params(account=account).perform()


def hasShare(session, baseurl, account, destination):
    """
    判断是否有分享关系
    :param session:
    :param baseurl:
    :param account:
    :param destination:
    :return:
    """
    url = _get_prefix(baseurl) + '_hasShare'
    return curl(url, session).method('post').headers(headers).params(account=account, destination=destination).perform()


def removeShare(session, baseurl, account, destination, s):
    """
    删除商户（移除分享关系）
    :param session:
    :param baseurl:
    :param account:
    :param destination:
    :param s:
    :return:
    """
    url = _get_prefix(baseurl) + '_removeShare'
    return curl(url, session).method('post').headers(headers).params(**{
        "account": account,
        "destination": destination,
        "string": s
    }).perform()


def removeShares(session, baseurl, account, s, destinations):
    """
    批量删除商户（移除分享关系）
    :param session:
    :param baseurl:
    :param account:
    :param s:
    :param destinations:
    :return:
    """
    url = _get_prefix(baseurl) + '_removeShares'
    return curl(url, session).method('post').headers(headers).params(**{
        "account": account,
        "string": s
    }).body(destinations).perform()


def saveShares(session, baseurl, account, s, destinations):
    """
    全量更新设置商户（分享关联关系） 删除之前所有分享关联的target 更新新的所有的
    :param session:
    :param baseurl:
    :param account:
    :param s:
    :param destinations:
    :return:
    """
    url = _get_prefix(baseurl) + '_saveShares'
    return curl(url, session).method('post').headers(headers).params(**{
        "account": account,
        "string": s
    }).body(destinations).perform()
