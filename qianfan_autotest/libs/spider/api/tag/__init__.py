# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def recent(session, baseurl, tenant, number):
    """
    最近使用标签列表
    :param session:
    :param baseurl:
    :param tenant:
    :param number:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/tag/recent/{number}".format(tenant=tenant, number=number)
    return curl(url, session).headers(headers).perform()


def remove(session, baseurl, tenant, body):
    """
    删除标签
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/tag/remove".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
