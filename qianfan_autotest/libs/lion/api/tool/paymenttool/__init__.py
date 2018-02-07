# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/tool/paymenttool"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, deviceId):
    """
    获取绑定信息
    :param session:
    :param baseurl:
    :param deviceId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(deviceId=deviceId).perform()
