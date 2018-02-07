# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, store, code):
    """
    模糊查询门店商品信息
    :param session:
    :param baseurl:
    :param tenant:
    :param store:
    :param code:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/{store}/query/skus'.format(tenant=tenant, store=store)
    return curl(url, session).headers(headers).params(code=code).perform()
