# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downLoadByBuilding(session, baseurl, bloc, body):
    """
    业态销售按报表下载 - 楼宇
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/downLoadByBuilding".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downLoadByFloor(session, baseurl, bloc, body):
    """
    业态销售按报表下载 - 楼层
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/downLoadByFloor".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downLoadByProject(session, baseurl, bloc, body):
    """
    业态销售按报表下载 - 项目
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/downLoadByProject".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downLoadByRegion(session, baseurl, bloc, body):
    """
    业态销售按报表下载 - 区域
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/downLoadByRegion".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downLoadByShop(session, baseurl, bloc, body):
    """
    业态销售按报表下载 - 商铺
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/downLoadByShop".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbybuilding(session, baseurl, bloc, body):
    """
    业态销售按楼宇报表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/reportbybuilding".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbyfloor(session, baseurl, bloc, body):
    """
    业态销售按楼层报表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/reportbyfloor".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbyproject(session, baseurl, bloc, body):
    """
    业态销售按项目报表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/reportbyproject".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbyregion(session, baseurl, bloc, body):
    """
    业态销售按区域报表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/reportbyregion".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbyshop(session, baseurl, bloc, body):
    """
    业态销售按商铺报表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/bcreport/reportbyshop".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
