# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def home(session, baseurl, tenant):
    """
    会员DPOS首页
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/home".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()
