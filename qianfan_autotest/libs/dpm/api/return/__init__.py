# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "return"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, uuid):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).method("post").headers(headers).body(uuid).perform()


def query(session, baseurl, qd):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method("post").headers(headers).body(qd).perform()
