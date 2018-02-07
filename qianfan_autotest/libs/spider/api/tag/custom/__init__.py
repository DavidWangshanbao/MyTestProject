# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, uuid):
    """
    获得自定义标签
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/tag/custom/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def list(session, baseurl, tenant):
    """
    自定义标签列表
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/tag/custom/list".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def modify(session, baseurl, tenant, body):
    """
    编辑自定义标签
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/tag/custom/modify".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def new(session, baseurl, tenant, body):
    """
    新增自定义标签
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/tag/custom/new".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
