# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "sg"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, guidepost):
    """
    通过指路牌获取产品销售URL，并利用浏览器特性通过HTTP code(307)自动重定向到产品销售地址
    :param session:
    :param baseurl:
    :param guidepost: 指路牌字符串
    :return:
    """
    url = _get_prefix(baseurl) + guidepost
    return curl(url, session).headers(headers).perform()
