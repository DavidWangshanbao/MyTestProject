# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def deposit(session, baseurl, tenant, body):
    """
    保存充值记录, 返回会员已存在：[new:false]，会员不存在：[new:true]
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/deposit".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def modify_deposit(session, baseurl, tenant, body):
    """
    改变充值单状态
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/deposit/modify".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def processing_deposit(session, baseurl, tenant, order_by):
    """
    未完成的充值单
    :param session:
    :param baseurl:
    :param tenant:
    :param order_by:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/deposit/processing".format(tenant=tenant)
    return curl(url, session).headers(headers).params(**{"order-by": order_by}).perform()


def list_regular_deposit(session, baseurl, tenant):
    """
    充值优惠规则列表
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/deposit/regular/list".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def modify_regular_deposit(session, baseurl, tenant, body):
    """
    充值优惠规则列表
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/deposit/regular/save/modify".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
