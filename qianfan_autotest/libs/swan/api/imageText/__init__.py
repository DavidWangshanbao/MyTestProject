# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def queryActivity(session, baseurl, tenant, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/imageText/queryActivity".format(tenant=tenant)
    return curl(url, session).headers(headers).params(shop=shop).perform()
