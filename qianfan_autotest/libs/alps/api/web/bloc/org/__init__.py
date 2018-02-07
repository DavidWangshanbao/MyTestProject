# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def disable(session, baseurl, bloc, uuid, version):
    """
    停用组织
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/disable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def enable(session, baseurl, bloc, uuid, version):
    """
    启用组织
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/enable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def getbyuuid(session, baseurl, bloc, uuid):
    """
    根据uuid查询组织
    :param session:
    :param baseurl:
    :param bloc:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/getbyuuid'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, body):
    """
    查询组织列表
    :param session:
    :param baseurl:
    :param bloc:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodify(session, baseurl, bloc, body):
    """
    修改组织
    :param session:
    :param baseurl:
    :param bloc:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/savemodify'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, body):
    """
    创建组织
    :param session:
    :param baseurl:
    :param bloc:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/savenew'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def switchorg(session, baseurl, bloc, userUuid, orgUuid):
    """
    创建组织
    :param session:
    :param baseurl:
    :param bloc:
    :param userUuid:
    :param orgUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/org/switchorg'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(userUuid=userUuid, orgUuid=orgUuid).perform()
