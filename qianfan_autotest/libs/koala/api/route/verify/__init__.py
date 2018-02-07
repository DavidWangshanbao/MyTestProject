# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/account"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def verifyPay(session, baseurl, s, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_verifyPay'
    return curl(url, session).method('post').params(**{"string": s}).body(body).perform()
