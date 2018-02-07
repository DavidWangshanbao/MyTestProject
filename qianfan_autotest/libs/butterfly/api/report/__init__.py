# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def sum(session, baseurl, tenant, keys, qc):
    """
    取得指定筛选条件下的合计
    :param session:
    :param baseurl:
    :param tenant:
    :param keys:
    :param qc:
    :return:
    """
    url = _get_prefix(baseurl) + "{tenant}/coupon_report/sum".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(keys=keys).body(qc).perform()


def query(session, baseurl, tenant, fetchParts, qd):
    """
    查询券统计报表
    :param session:
    :param baseurl:
    :param tenant:
    :param fetchParts:
    :param qd:
    :return:
    """
    url = _get_prefix(baseurl) + "{tenant}/coupon_report/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(keys=fetchParts).body(qd).perform()
