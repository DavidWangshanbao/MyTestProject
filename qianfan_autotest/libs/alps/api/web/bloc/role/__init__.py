# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def delete(session, baseurl, bloc, roleUuid, version):
    """
    删除角色和角色功能权限
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param roleUuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/delete'.format(bloc=bloc)
    return curl(url, session).method('delete').headers(headers).params(roleUuid=roleUuid, version=version).perform()


def delete(session, baseurl, bloc, roleUuid, userUuid):
    """
    移除角色包含用户
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param roleUuid:
    :param userUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/delete'.format(bloc=bloc)
    return curl(url, session).method('delete').headers(headers).params(roleUuid=roleUuid, userUuid=userUuid).perform()


def query(session, baseurl, bloc, body, userUuid):
    """
    查询角色列表-分页查询
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :param userUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(userUuid=userUuid).body(body).perform()


def queryalluser(session, baseurl, bloc, roleUuid, userUuid, orgUuid, keyword):
    """
    新增角色包含用户-查询用户
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param roleUuid:
    :param userUuid:
    :param orgUuid:
    :param keyword:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/queryalluser'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(roleUuid=roleUuid, userUuid=userUuid,
                                                      orgUuid=orgUuid, keyword=keyword).perform()


def queryrolepermissions(session, baseurl, bloc, roleUuid, userUuid, orgUuid):
    """
    查询角色功能权限
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param roleUuid:
    :param userUuid:
    :param orgUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/queryrolepermissions'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(roleUuid=roleUuid, userUuid=userUuid,
                                                      orgUuid=orgUuid).perform()


def queryroles(session, baseurl, bloc, keyword, userUuid, orgUuid):
    """
    查询角色列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param keyword:
    :param userUuid:
    :param orgUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/queryroles'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(keyword=keyword, userUuid=userUuid,
                                                      orgUuid=orgUuid).perform()


def queryroleusers(session, baseurl, bloc, roleUuid):
    """
    查询包含用户
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param roleUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/queryroles'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(roleUuid=roleUuid).perform()


def savemodifyrole(session, baseurl, bloc, body):
    """
    修改角色
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/savemodifyrole'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenewrole(session, baseurl, bloc, body):
    """
    新建角色
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/savenewrole'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenewroleusers(session, baseurl, bloc, body):
    """
    新增角色包含用户
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/savenewroleusers'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saverolepermission(session, baseurl, bloc, body):
    """
    保存角色功能权限
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/role/saverolepermission'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
