# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "service/1/account-transactions"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def listByRequestId(session, baseurl, tenant, requestid):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "by-request-id/{requestid}".format(requestid=requestid)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def listByTransId(session, baseurl, tenant, ns, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "by-trans/{ns},{id}".format(ns=ns, id=id)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def query(session, baseurl, tenant, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(body).params(tenant=tenant).perform()
