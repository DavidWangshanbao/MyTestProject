# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/health"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def open(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + '{tenant}/smcAccount/open'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get(session, baseurl, tenant):
    url = _get_prefix(baseurl) + '{tenant}/smcAccount/get'.format(tenant=tenant)
    return curl(url, session).headers(headers).perform()
