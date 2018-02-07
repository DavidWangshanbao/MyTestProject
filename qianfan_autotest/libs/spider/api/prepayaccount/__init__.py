# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl

def adjust_balance(session,baseurl,tenant,body):
    """
    调整账户余额
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/prepayaccount/balance/adjustment".format(tenant=tenant)
    return curl(url,session).method('post').headers(headers).body(body).perform()

def details(session,baseurl,tenant,body):
    """
    获得账户变动名细
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/prepayaccount/details".format(tenant=tenant)
    return curl(url,session).method('post').headers(headers).body(body).perform()

def freeze(session,baseurl,tenant,member,shop):
    """
    冻结账户
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/prepayaccount/freeze".format(tenant=tenant)
    return curl(url,session).headers(headers).params(member=member,shop=shop).perform()

def general(session,baseurl,tenant,member):
    """
    获得账户概要信息
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/prepayaccount/general".format(tenant=tenant)
    return curl(url, session).headers(headers).params(member=member).perform()

def unfreeze(session,baseurl,tenant,member,shop):
    """
    解冻账户
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/prepayaccount/unfreeze".format(tenant=tenant)
    return curl(url,session).headers(headers).params(member=member,shop=shop).perform()