# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def cardApiSignature(session, baseurl, tenant, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/wx/cardApiSignature".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def jsapiSignature(session, baseurl, tenant, url):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/wx/jsapiSignature".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(url=url).perform()
