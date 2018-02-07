# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getByOpenId(session, baseurl, tenant, shop, openid):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/getByOpenId".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(shop=shop, openid=openid).perform()


def register(session, baseurl, tenant, shop, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/register".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).params(shop=shop).perform()
