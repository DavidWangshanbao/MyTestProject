# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc, project, uuid):
    """
    获取采集点日志文件
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctlog/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询采集点日志
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctlog/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, bloc, project, uuid):
    """
    删除采集点日志
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctlog/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid).perform()
