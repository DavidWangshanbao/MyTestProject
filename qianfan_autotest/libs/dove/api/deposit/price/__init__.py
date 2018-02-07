# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/depositprice"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getPrice(session, baseurl):
    url = _get_prefix(baseurl) + 'getPrice'
    return curl(url, session).headers(headers).perform()


def getAllCombos(session, baseurl):
    url = _get_prefix(baseurl) + 'getAllCombos'
    return curl(url, session).headers(headers).perform()
