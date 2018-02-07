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
    查询采集点指令
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctcommand/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询采集点指令列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctcommand/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def querycancancelcommand(session, baseurl, bloc, project, collectionTerminalNos):
    """
    查询可作废指令列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param collectionTerminalNos:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctcommand/querycancancelcommand'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(
        collectionTerminalNos=collectionTerminalNos).perform()


def querycancancelct(session, baseurl, bloc, project):
    """
    新建作废指令_查询采集点列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctcommand/querycancancelct'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).perform()


def remove(session, baseurl, bloc, project, uuid):
    """
    删除采集点指令
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctcommand/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    修改采集点指令
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ctcommand/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, project, body):
    """
    新建采集点指令
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/savenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def syncstate(session, baseurl, bloc, project, uuid, state):
    """
    同步指令状态
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :param state:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/syncstate'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, state=state).perform()
