# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl,headers

PREFIX = 'web/health'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def health_check(session, baseurl):
    """
    健康检查
    :return:
    """
    baseurl = _get_prefix(baseurl)
    url = baseurl + 'check'
    # return session.get(url, timeout=5)
    return curl(url).headers(headers).perform()
