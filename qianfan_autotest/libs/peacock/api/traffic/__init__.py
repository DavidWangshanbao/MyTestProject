# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def summary(session, baseurl, tenant, organizer, body):
    """
    流量统计
    :param session:
    :param baseurl:
    :param tenant:
    :param organizer:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/traffic/summary'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organizer=organizer).body(body).perform()
