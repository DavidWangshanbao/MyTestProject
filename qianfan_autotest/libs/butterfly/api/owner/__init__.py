# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getTotal(session, baseurl, tenant, ownerNamespace, ownerId):
    url = _get_prefix(baseurl) + "{tenant}/owner_coupon/total".format(tenant=tenant)
    return curl(url, session).headers(headers).params(owner_namespace=ownerNamespace, owner_id=ownerId).perform()


def queryCoupon(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/owner_coupon/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
