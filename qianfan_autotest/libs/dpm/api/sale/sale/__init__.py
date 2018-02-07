# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "sale/sale"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, uuid):
    url = _get_prefix(baseurl) + 'get'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, qd):
    url = _get_prefix(baseurl) + 'query'
    return curl(url, session).method('post').headers(headers).body(qd).perform()
