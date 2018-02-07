# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query_building(session, baseurl, bloc, body):
    """
    查询集团楼宇
    :param sessoin:
    :param baseurl:
    :param bloc:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/building/query".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query_floor(session, baseurl, bloc, body):
    """
    查询集团楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/floor/query".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
