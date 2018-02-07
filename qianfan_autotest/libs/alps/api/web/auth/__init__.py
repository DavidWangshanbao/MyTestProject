# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/auth"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def login(session, baseurl, bloc, body):
    """
    登录
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/login".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def logout(session, baseurl, bloc):
    """
    登出
    :param session:
    :param baseurl:
    :param bloc: 集团
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/logout".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).perform()


def getorg(session, baseurl, body):
    """
    获取用户组织
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getorg"
    return curl(url, session).method('post').headers(headers).body(body).perform()
