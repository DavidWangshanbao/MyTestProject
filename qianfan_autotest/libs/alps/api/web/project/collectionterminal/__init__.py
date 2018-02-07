# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def cancelcheckaccepted(session, baseurl, bloc, project, uuid, version):
    """
    取消验收采集点
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/cancelcheckaccepted'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def checkaccpted(session, baseurl, bloc, project, uuid, version):
    """
     验证采集点
    :param sessioin:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/checkaccpted'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def copy(session, baseurl, bloc, project, body):
    """
     复制采集点
    :param sessioin:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/copy'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def disable(session, baseurl, bloc, project, uuid, version):
    """
     停用采集点
    :param sessioin:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/disable'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def enable(session, baseurl, bloc, project, uuid, version):
    """
     采用采集点
    :param sessioin:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/enable'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def get(session, baseurl, bloc, project, uuid):
    """
    查询采集点
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询采集点列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def querynumbers(session, baseurl, bloc, project, body):
    """
    查询采集点编号列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/querynumbers'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    修改采集点
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, project, body):
    """
     新建采集点
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/savenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def uninstall(session, baseurl, bloc, project, uuid, version):
    """
    卸载采集点
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/collectionterminal/uninstall'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()
