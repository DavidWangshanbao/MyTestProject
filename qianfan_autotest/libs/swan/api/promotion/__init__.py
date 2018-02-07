# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def queryActivity(session, baseurl, tenant, shop):
    """
    有效促销活动
    :param session:
    :param baseurl:
    :param tenant:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/promotion/queryActivity".format(tenant=tenant)
    return curl(url, session).headers(headers).params(shop=shop).perform()
