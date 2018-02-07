# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downloadSummary(session, baseurl, bloc, project, body):
    """
    总销售报表下载
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salesummary/downloadSummary'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def summary(session, baseurl, bloc, project, body):
    """
    总销售额
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/salesummary/summary'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
