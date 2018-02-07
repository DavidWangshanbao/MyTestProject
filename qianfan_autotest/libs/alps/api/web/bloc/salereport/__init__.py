# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downloadByBuilding(session, baseurl, bloc, body):
    """
    会员销售按楼宇报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/downloadByBuilding'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByFloor(session, baseurl, bloc, body):
    """
    会员销售按楼层报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/downloadByFloor'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByProject(session, baseurl, bloc, body):
    """
    会员销售按项目报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/downloadByProject'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByRegion(session, baseurl, bloc, body):
    """
    会员销售按区域报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/downloadByRegion'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByShop(session, baseurl, bloc, body):
    """
    会员销售按商铺报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/downloadByShop'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbybuilding(session, baseurl, bloc, body):
    """
    会员销售按楼宇报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/salereportbybuilding'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbyfloor(session, baseurl, bloc, body):
    """
    会员销售按楼层报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/salereportbyfloor'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbyproject(session, baseurl, bloc, body):
    """
    会员销售按项目报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/salereportbyproject'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbyregion(session, baseurl, bloc, body):
    """
    会员销售按区域报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/salereportbyregion'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbyshop(session, baseurl, bloc, body):
    """
    会员销售按商铺报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/salereport/salereportbyshop'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
