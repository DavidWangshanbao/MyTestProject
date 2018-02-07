# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/serviceprovider/device/tag"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, type):
    """
    设备标记列表
    :param session:
    :param baseurl:
    :param type:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).headers(headers).params(type=type).perform()


def saveNew(session, baseurl, type, code, name):
    """
    新增设备标记
    :param session:
    :param baseurl:
    :param type:
    :param code:
    :param name:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'saveNew'
    return curl(url, session).method('post').headers(headers).params(type=type, code=code, name=name).perform()


def test(session, baseurl, code):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'test'
    return curl(url, session).method('post').headers(headers).params(code=code).perform()
