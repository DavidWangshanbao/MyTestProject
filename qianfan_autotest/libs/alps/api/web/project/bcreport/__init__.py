# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downByBuilding(session, baseurl, bloc, project, body):
    """
    业态销售按报表下载 - 楼宇
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/bcreport/downByBuilding".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downByFloor(session, baseurl, bloc, project, body):
    """
    业态销售按报表下载 - 楼层
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/bcreport/downByFloor".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downByShop(session, baseurl, bloc, project, body):
    """
    业态销售按报表下载 - 商铺
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/bcreport/downByShop".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbybuilding(session, baseurl, bloc, project, body):
    """
    业态销售按楼宇报表
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/bcreport/reportbybuilding".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbyfloor(session, baseurl, bloc, project, body):
    """
    业态销售按楼层报表
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/bcreport/reportbyfloor".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reportbyshop(session, baseurl, bloc, project, body):
    """
    业态销售按商铺报表
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/bcreport/reportbyshop".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
