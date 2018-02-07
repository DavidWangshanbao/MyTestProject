# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/prepay-web/1/reports"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def sumAmounts(session, baseurl, tenant, body, rsfetchParts):
    url = _get_prefix(baseurl) + 'sum-amounts'
    return curl(url, session).method('post').headers(headers).params(rsfetchParts=rsfetchParts, tenant=tenant).body(
        body).perform()


def sumCounts(session, baseurl, tenant, body, rsfetchParts):
    url = _get_prefix(baseurl) + 'sum-counts'
    return curl(url, session).method('post').headers(headers).params(rsfetchParts=rsfetchParts, tenant=tenant).body(
        body).perform()


def query(session, baseurl, tenant, body, rsfetchParts):
    url = _get_prefix(baseurl) + 'query'
    return curl(url, session).method('post').headers(headers).params(rsfetchParts=rsfetchParts, tenant=tenant).body(
        body).perform()
