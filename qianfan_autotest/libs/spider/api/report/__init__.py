# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def shop_count(session, baseurl, tenant, shop):
    """
    门店维度统计
    :param session:
    :param baseurl:
    :param tenant:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/report/count/shop".format(tenant=tenant)
    return curl(url, session).headers(headers).params(shop=shop).perform()


def tenant_count(session, baseurl, tenant):
    """
    租户维度统计
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/report/count/tenant".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def today_count(session, baseurl, tenant):
    """
    今日统计
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/report/count/today".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def shop_daily(session, baseurl, tenant, shop, body):
    """
    门店时间维度报表
    :param session:
    :param baseurl:
    :param tenant:
    :param shop:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/report/daily/shop".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(shop=shop).body(body).perform()
