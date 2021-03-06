# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/prepay-web/health"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check(session, baseurl, sensitive=None):
    url = _get_prefix(baseurl) + "check"
    ocurl = curl(url, session).headers(headers)
    if sensitive:
        ocurl.params(sensitive=sensitive)
    return ocurl.perform()
