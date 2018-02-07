# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def applytemplatenew(session, baseurl, bloc, project, body):
    """
    应用模板新建销售计划
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplan/applytemplatenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def batchnew(session, baseurl, bloc, project, body):
    """
    批量新建销售计划
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplan/batchnew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询销售计划
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplan/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def queryByYear(session, baseurl, bloc, project, year):
    """
    查询年销售计划
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param year:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplan/queryByYear'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(year=year).perform()


def savemodify(session, baseurl, bloc, project, date, amount):
    """
    查询年销售计划
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param date:
    :param amount:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplan/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(date=date, amount=amount).perform()
