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
    获得商户偏好
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/get".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def getTenantConfig(session, baseurl, tenant):
    """
    获得商户配置(权益开通情况)
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/getTenantConfig".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def save(session, baseurl, tenant, body):
    """
    保存商户偏好
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/preference/save".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
