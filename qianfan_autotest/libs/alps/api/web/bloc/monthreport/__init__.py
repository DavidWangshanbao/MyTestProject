# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downlaodByMonth(session, baseurl, bloc, body):
    """
    月报表 - 下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/monthreport/downlaodByMonth'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbymonth(session, baseurl, bloc, body):
    """
    月报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/monthreport/reportbymonth'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
