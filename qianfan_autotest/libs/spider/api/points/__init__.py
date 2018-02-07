# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def adjust(session, baseurl, tenant, body):
    """
    调整积分账户余额
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/points/adjust".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query(session, baseurl, tenant, body):
    """
    查询会员积分流水
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/points/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get_memeber(session, baseurl, tenant, memberId):
    """
    查询会员积分余额
    :param session:
    :param baseurl:
    :param tenant:
    :param memberId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/points/member/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(memberId=memberId).perform()


def get_tenant(session, baseurl, tenant):
    """
    查询租户级会员余额
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/points/tenant/get".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()
