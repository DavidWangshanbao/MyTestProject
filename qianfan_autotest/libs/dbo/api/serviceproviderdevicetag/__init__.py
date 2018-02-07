# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/web/serviceprovider/device/tag"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getByCode(session, baseurl, type, code):
    """
    设备标记列表
    :param session:
    :param baseurl:
    :param type:
    :param code:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getByCode"
    return curl(url, session).headers(headers).params(type=type, code=code).perform()


def query(session, baseurl, type):
    """

    :param session:
    :param baseurl:
    :param type:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).headers(headers).params(type=type).perform()


def saveNew(session, baseurl, body):
    """
    新建设备标记
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "saveNew"
    return curl(url, session).method('post').headers(headers).body(body).perform()
