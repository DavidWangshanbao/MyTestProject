# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "weixin/qrcode"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def image(session, baseurl):
    url = _get_prefix(baseurl) + "image"
    return curl(url, session).headers(headers).perform()
