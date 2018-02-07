# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def open(session, baseurl, tenant):
    """
    开通储值支付
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/open".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).perform()


def opened(session, baseurl, tenant):
    """
    查询是否已开通储值频道
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/opened".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()
