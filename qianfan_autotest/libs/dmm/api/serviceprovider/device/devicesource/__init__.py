# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/serviceprovider/device/devicesource"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def list(session, baseurl):
    """
    设备类型列表
    :param session:
    :param baseurl:
    :return: list of BUcn
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'list'
    return curl(url, session).headers(headers).perform()
