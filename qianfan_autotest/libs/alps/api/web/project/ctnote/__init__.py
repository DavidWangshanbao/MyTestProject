# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def queryctnotes(session, baseurl, bloc, project, body):
    """
    查看采集点操作日志列表
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctlog/queryctnotes'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodifybyclearnote(session, baseurl, bloc, project, uuid, version):
    """
    清除采集点备注(添加采集点备注日志)
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctlog/savemodifybyclearnote'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def savenewnote(session, baseurl, bloc, project, body):
    """
    查看采集点操作日志列表
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctlog/savenewnote'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
