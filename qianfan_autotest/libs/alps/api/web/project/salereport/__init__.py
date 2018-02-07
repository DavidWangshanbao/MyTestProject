# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downloadByBuilding(session, baseurl, bloc, project, body):
    """
    会员销售按楼宇报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salereport/downloadByBuilding'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadByFloor(session, baseurl, bloc, project, body):
    """
    会员销售按楼层报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salereport/downloadByFloor'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadBuShop(session, baseurl, bloc, project, body):
    """
    会员销售按商铺报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salereport/downloadBuShop'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbybuilding(session, baseurl, bloc, project, body):
    """
    会员销售按楼宇报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salereport/salereportbybuilding'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbyfloor(session, baseurl, bloc, project, body):
    """
    会员销售按楼层报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salereport/salereportbyfloor'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def salereportbyshop(session, baseurl, bloc, project, body):
    """
    会员销售按商铺报表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salereport/salereportbyshop'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
