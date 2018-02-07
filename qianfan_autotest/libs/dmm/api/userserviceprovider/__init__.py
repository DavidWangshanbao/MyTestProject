# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/userserviceprovider"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getByUser(session, baseurl, usr):
    """
    服务商列表
    :param session:
    :param baseurl:
    :param usr:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getByUser'
    return curl(url, session).headers(headers).params(user=usr).perform(timeout=5)
