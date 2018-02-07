# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def queryreport(session, baseurl, bloc, body):
    """
    报表查询
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/index/queryreport'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def querytotalcount(session, baseurl, bloc, body):
    """
    总数查询
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/index/querytotalcount'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
