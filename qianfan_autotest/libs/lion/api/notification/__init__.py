# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/notification"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def invites(session, baseurl):
    """
    查询入店邀请
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "invites"
    return curl(url, session).headers(headers).perform()


def process(session, baseurl, id, code):
    """
    处理入店邀请
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + id
    return curl(url, session).method('post').headers(headers).params(code=code).perform()
