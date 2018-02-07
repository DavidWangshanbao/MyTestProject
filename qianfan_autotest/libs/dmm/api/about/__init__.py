# coding=utf-8
from __future__ import unicode_literals, print_function

PREFIX = ""
from utils import baseurl_strip, curl, headers


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def about(session, baseurl, auth=None):
    """

    :param session: requests session object
    :param baseurl:
    :param auth:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'about'

    if auth:
        return curl(url, session).headers(headers).perform(verify=False, auth=auth)
    else:
        return curl(url, session).headers(headers).perform(verify=False)
