# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def delete(session, baseurl, bloc, userUuid, version):
    """
    删除用户、用户赋予角色和用户功能权限
    :param session:
    :param baseurl:
    :param bloc:
    :param userUuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/delete'.format(bloc=bloc)
    return curl(url, session).method('delete').headers(headers).params(userUuid=userUuid, version=version).perform()


def disable(session, baseurl, bloc, userUuid, version):
    """
    停用用户
    :param session:
    :param baseurl:
    :param bloc:
    :param userUuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/disable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(userUuid=userUuid, version=version).perform()


def enable(session, baseurl, bloc, userUuid, version):
    """
    启用用户
    :param session:
    :param baseurl:
    :param bloc:
    :param userUuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/enable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(userUuid=userUuid, version=version).perform()


def getallmgrorgs(session, baseurl, bloc, userUuid):
    """
    查询所管理组织
    :param session:
    :param baseurl:
    :param bloc:集团
    :param userUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/getallmgrorgs'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(userUuid=userUuid).perform()


def getmgrorgs(session, baseurl, bloc, userUuid):
    """
    查询所属组织
    :param session:
    :param baseurl:
    :param bloc:集团
    :param userUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/getmgrorgs'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(userUuid=userUuid).perform()


def getusablerolesbyuser(session, baseurl, bloc, userUuid):
    """
    查询包含角色列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param userUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/getusablerolesbyuser'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(userUuid=userUuid).perform()


def query(session, baseurl, bloc, userUuid, body):
    """
    查询用户列表-分页查询
    :param session:
    :param baseurl:
    :param bloc:集团
    :param userUuid:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(userUuid=userUuid).body(body).perform()


def queryuserpermissions(session, baseurl, bloc, fromUserUuid, toUserUuid, orgUuid):
    """
    查询用户功能权限
    :param session:
    :param baseurl:
    :param bloc:集团
    :param fromUserUuid:
    :param toUserUuid:
    :param orgUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/queryuserpermissions'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(orgUuid=orgUuid, fromUserUuid=fromUserUuid,
                                                      toUserUuid=toUserUuid).perform()


def queryuserroles(session, baseurl, bloc, fromUserUuid, toUserUuid):
    """
    查询赋予角色列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param fromUserUuid:
    :param toUserUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/queryuserroles'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(fromUserUuid=fromUserUuid,
                                                      toUserUuid=toUserUuid).perform()


def queryusers(session, baseurl, bloc, fromUserUuid, toUserUuid, keyword):
    """
    查询用户列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param fromUserUuid:
    :param toUserUuid:
    :param keyword:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/queryuserpermissions'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(keyword=keyword, fromUserUuid=fromUserUuid,
                                                      toUserUuid=toUserUuid).perform()


def resetpassword(session, baseurl, bloc, body):
    """
    重置密码
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/resetpassword'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodifypassword(session, baseurl, bloc, body):
    """
    修改密码
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/savemodifypassword'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodifyuser(session, baseurl, bloc, body):
    """
    修改用户
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/savemodifyuser'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenewuser(session, baseurl, bloc, body):
    """
    创建用户
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/savenewuser'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savepermission(session, baseurl, bloc, body):
    """
    修改用户功能权限
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/savepermission'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveuserroles(session, baseurl, bloc, body):
    """
    修改用户赋予角色
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/user/saveuserroles'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
