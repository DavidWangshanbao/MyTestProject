# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getsampleimage(session, baseurl, bloc, project, ticketUuid):
    """
    获取小票样例图
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param ticketUuid: String
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/syssampleimage/getsampleimage'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(ticketUuid=ticketUuid).perform()


def querytickets(session, baseurl, bloc, project, body):
    """
    查询小票样例列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/syssampleimage/querytickets'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def usesampleimage(session, baseurl, bloc, project, ticketUuid):
    """
    使用小票样例图
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param ticketUuid: String
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/syssampleimage/usesampleimage'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(ticketUuid=ticketUuid).perform()
