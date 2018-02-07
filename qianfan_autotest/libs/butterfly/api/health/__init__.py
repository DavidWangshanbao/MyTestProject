# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/health"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check(session, baseurl, sensitive=None):
    url = _get_prefix(baseurl) + "check"
    ocurl = curl(url, session).headers(headers)
    if sensitive:
        ocurl.params(sensitive=sensitive)
    ocurl.perform()


def alive(session, baseurl):
    url = _get_prefix(baseurl) + "alive"
    return curl(url, session).headers(headers).perform()
