# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/prepay-web/1/owner-transactions"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def listByRequestId(session, baseurl, tenant, requestId):
    url = _get_prefix(baseurl) + "by-requestId/{id}".format(id=requestId)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def listByTransId(session, baseurl, tenant, transNs, transId):
    url = _get_prefix(baseurl) + "by-transId/{ns},{id}".format(ns=transNs, id=transId)
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).perform()


def query(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "query"
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()
