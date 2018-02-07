# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, organizer):
    """
    业态判断
    :param session:
    :param baseurl:
    :param tenant:
    :param organizer:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/channels/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(organizer=organizer).perform()
