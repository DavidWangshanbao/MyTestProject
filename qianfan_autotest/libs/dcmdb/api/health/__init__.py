# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "health"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def health_check(baseurl):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'check'
    return curl(url).headers(headers).perform()
