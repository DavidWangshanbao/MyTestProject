# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def disable_build(session, baseurl, bloc, project, uuid, version):
    """
    禁止楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/disable".format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def enable_building(session, baseurl, bloc, project, uuid, version):
    """
    启用楼宇
    :param session:
    :param baseurl:
    :param bloc:  集团
    :param project:  项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/enable".format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def get_building(session, baseurl, bloc, project, uuid):
    """
    查询楼宇详情
    :param session:
    :param baseurl:
    :param bloc:  集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/get".format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query_building(session, baseurl, bloc, project, body):
    """
    查询楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/query".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove_building(session, baseurl, bloc, project, uuid, version):
    """
    删除楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/remove".format(bloc=bloc, project=project)
    return curl(url, session).method('delete').headers(headers).params(uuid=uuid, version=version).perform()


def savemodify_building(session, baseurl, bloc, project, body):
    """
    修改楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/savemodify".format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def savenew_building(session, baseurl, bloc, project, body):
    """
    新建楼宇
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/building/savenew".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def disable_floor(session, baseurl, bloc, project, uuid, version):
    """
    禁用楼层
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/disable".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def enable_floor(session, baseurl, bloc, project, uuid, version):
    """
    启用楼层
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/enable".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def get_floor(session, baseurl, bloc, project, uuid):
    """
    查询楼层
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/get".format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query_floor(session, baseurl, bloc, project, body):
    """
    查询楼层
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/query".format(bloc=bloc, project=project)
    return curl(url, session).method('post').body(body).perform()


def remove_floor(session, baseurl, bloc, project, uuid, version):
    """
    删除楼层
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/query".format(bloc=bloc, project=project)
    return curl(url, session).method('delete').headers(headers).params(uuid=uuid, version=version).perform()


def savemodify_floor(session, baseurl, bloc, project, body):
    """
    修改楼层
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/savemodify".format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def savenew_floor(session, baseurl, bloc, project, body):
    """
    修改楼层
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/floor/savenew".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
