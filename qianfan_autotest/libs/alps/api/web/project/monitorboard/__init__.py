# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getrunstatebyday(session, baseurl, bloc, project, collectionTerminalNo):
    """

    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param collectionTerminalNo: 采集点
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/dc/monitorboard/getrunstatebyday'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(collectionTerminalNo=collectionTerminalNo).perform()


def getsummary(session, baseurl, bloc, project):
    """
    查询后端监控看板今日概况
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/dc/monitorboard/getsummary'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).perform()


def queryct(session, baseurl, bloc, project, body):
    """
    查询后端监控看板列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/dc/monitorboard/queryct'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()

def query(session,baseurl,bloc,project):
    """

    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/monitorboard/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).perform()


def querylist(session,baseurl,bloc,project,body):
    """

    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/monitorboard/querylist'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
