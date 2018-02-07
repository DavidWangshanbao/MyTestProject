# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def articlesaleamount(session, baseurl, bloc, project, body):
    """
    商品按销售额汇总
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/articlereport/articlesaleamount".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def articlesaledetail(session, baseurl, bloc, project, body):
    """
    商品销售明细
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/articlereport/articlesaledetail".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadDetails(session, baseurl, bloc, project, body):
    """
    商品销售明细报表下载
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/articlereport/downloadDetails".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadSummary(session, baseurl, bloc, project, body):
    """
    商品按销售额汇总报表下载
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/articlereport/downloadSummary".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
