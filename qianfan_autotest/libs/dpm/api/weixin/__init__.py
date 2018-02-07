# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "weixin"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def qrcode(session, baseurl):
    """
    获取公众号二维码地址。
销售号可以通过关注此二维码，查看分润账单。
    :param session:
    :param baseurl:
    :return:
    """
    url = _get_prefix(baseurl) + "qrcode"
    return curl(url, session).headers(headers).perform()


def winxinmessage(session, baseurl, name):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'winxinmessage'
    return curl(url, session).method('post').headers(headers).body(name).perform()
