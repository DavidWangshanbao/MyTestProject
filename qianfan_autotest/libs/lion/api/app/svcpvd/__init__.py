# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/svcPvd"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def bindCode(session, baseurl, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "bindCode"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def list(session, baseurl, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "list"
    return curl(url, session).headers(headers).params(shop=shop).perform()
