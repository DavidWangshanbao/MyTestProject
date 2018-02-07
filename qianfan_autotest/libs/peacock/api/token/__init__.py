# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def test(session,baseurl,user):
    """
    测试token
    :param session:
    :param baseurl:
    :param user:
    :return:
    """
    _baseurl= _get_prefix(baseurl)
    url = _baseurl + "{user}/token/test".format(user=user)
    return curl(url,session).headers(headers).perform()
