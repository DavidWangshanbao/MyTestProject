# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def queryavailabledatasource(session, baseurl, bloc, userUuid, body):
    """
    查询可用数据源
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param userUuid:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscription/queryavailabledatasource'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(userUuid=userUuid).body(body).perform()


def querydatasourceparameters(session, baseurl, bloc, dataSourceUuids):
    """
    查询订阅数据源(展开)
    :param session:
    :param baseurl:
    :param bloc:
    :param dataSourceUuids:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscription/querydatasourceparameters'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(dataSourceUuids=dataSourceUuids).perform()


def querydatasourceparameters2(session, baseurl, bloc, dataSourceUuids):
    """
    查询订阅数据源（平铺）
    :param session:
    :param baseurl:
    :param bloc:
    :param dataSourceUuids:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscription/querydatasourceparameters2'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(dataSourceUuids=dataSourceUuids).perform()


def querydatasourceunn(session, baseurl, bloc, userUuid, method):
    """
    查询订阅数据源uuid,编号,名称

    :param session:
    :param baseurl:
    :param bloc:
    :param userUuid:
    :param method:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscription/querydatasourceunn'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(userUuid=userUuid, method=method).perform()
