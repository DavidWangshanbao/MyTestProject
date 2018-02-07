# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def change_list(session, baseurl, tenant, body):
    """
    优惠券变动列表
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/change/list".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def expiry_list(session, baseurl, tenant, member):
    """
    有效优惠券列表
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/expiry/list".format(tenant=tenant)
    return curl(url, session).headers(headers).params(member=member).perform()
