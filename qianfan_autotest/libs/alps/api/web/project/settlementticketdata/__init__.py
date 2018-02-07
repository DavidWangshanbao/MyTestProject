# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getbyfeaturecode(session, baseurl, bloc, project, featureCode):
    """
    根据特征码查询日结小票数据
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param featureCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementticketdata/getbyfeaturecode'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(featureCode=featureCode).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询日结小票列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementticketdata/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reprocess(session, baseurl, bloc, project, featureCode):
    """
    日结小票重新加工
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param featureCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementticketdata/reprocess'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(featureCode=featureCode).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    修改日结小票数据
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementticketdata/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
