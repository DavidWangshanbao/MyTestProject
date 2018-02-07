# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def judge_holiday(session, baseurl, tenant, date):
    """
    法定节假日判断
    :param session:
    :param baseurl:
    :param tenant:
    :param date:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/holiday/judge_holidy'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(date=date).perform()
