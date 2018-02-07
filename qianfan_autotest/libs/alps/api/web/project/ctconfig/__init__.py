# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc, project, collectionTerminalNo):
    """
    采集点配置查询
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param collectionTerminalNo:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctconfig/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(collectionTerminalNo=collectionTerminalNo).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    采集点配置
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctconfig/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
