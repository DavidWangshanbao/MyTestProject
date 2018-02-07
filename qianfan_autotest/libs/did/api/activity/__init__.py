# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/activity"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getAnswer(session, baseurl, openId):
    """
    取得用户答案
    :param session:
    :param baseurl:
    :param openId:
    :return:
    """
    url = _get_prefix(baseurl) + 'getAnswer'
    return curl(url, session).headers(headers).params(openId=openId).perform()


def getLotteryRecord(session, baseurl):
    """
    获取用户最新的抽奖记录结果
    :param session:
    :param baseurl:
    :return:
    """
    url = _get_prefix(baseurl) + 'getLotteryRecord'
    return curl(url, session).headers(headers).perform()


def lottery(session, baseurl):
    """
    抽奖
    :param session:
    :param baseurl:
    :return:
    """
    url = _get_prefix(baseurl) + 'lottery'
    return curl(url, session).headers(headers).perform()


def submitAnswer(session, baseurl, resultId):
    """
    提交答案
    :param session:
    :param baseurl:
    :param resultId:
    :return:
    """
    url = _get_prefix(baseurl) + 'submitAnswer'
    return curl(url, session).method('post').headers(headers).params(resultId=resultId).perform()
