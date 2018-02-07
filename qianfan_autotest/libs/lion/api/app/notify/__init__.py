# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/notify"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, body):
    """
    查询系统通知列表
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def read(session, baseurl, id):
    """
    阅读指定消息
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "read"
    return curl(url, session).headers(headers).params(id=id).perform()
