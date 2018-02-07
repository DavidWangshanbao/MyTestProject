# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant):
    """
    积分服务是否开通查询
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/points/get".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def open(session, baseurl, tenant, body):
    """
    开通积分服务
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/points/open".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get_rules(session, baseurl, tenant):
    """
    查询积分规则
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/points/rule/get".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def save_rule(session, baseurl, tenant, body):
    """
    保存积分规则
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/points/rule/save".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
