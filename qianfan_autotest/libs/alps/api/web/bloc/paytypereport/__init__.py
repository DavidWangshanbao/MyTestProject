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
    付款方式销售报表 - 按楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/downloadByBuilding'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByFloor(session, baseurl, bloc, body):
    """
    付款方式销售报表 - 按楼层
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/downloadByFloor'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByProject(session, baseurl, bloc, body):
    """
    付款方式销售报表 - 按项目
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/downloadByProject'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByRegion(session, baseurl, bloc, body):
    """
    付款方式销售报表 - 按区域
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/downloadByRegion'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByShop(session, baseurl, bloc, body):
    """
    付款方式销售报表 - 按商铺
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/downloadByShop'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def paytypereportbybuilding(session, baseurl, bloc, body):
    """
    业态销售按楼宇报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/paytypereportbybuilding'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def paytypereportbyfloor(session, baseurl, bloc, body):
    """
    业态销售按楼层报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/paytypereportbyfloor'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def paytypereportbyproject(session, baseurl, bloc, body):
    """
    业态销售按项目报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/paytypereportbyproject'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def paytypereportbyregion(session, baseurl, bloc, body):
    """
    业态销售按区域报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/paytypereportbyregion'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def paytypereportbyshop(session, baseurl, bloc, body):
    """
    业态销售按商户报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytypereport/paytypereportbyshop'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
