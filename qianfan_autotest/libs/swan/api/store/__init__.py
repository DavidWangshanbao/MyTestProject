# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/store/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(shop=shop).perform()
