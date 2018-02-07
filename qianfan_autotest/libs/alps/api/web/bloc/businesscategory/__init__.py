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
    停用业态
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/businesscategory/disable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def enable(session, baseurl, bloc, uuid, version):
    """
    启用业态
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/businesscategory/enable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def get(session, baseurl, bloc, uuid):
    """
    查询业态详情
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/businesscategory/get'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, body):
    """
    查询业态
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/businesscategory/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodify(session, baseurl, bloc, body):
    """
    修改业态
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/businesscategory/savemodify'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, body):
    """
    创建业态
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/businesscategory/savenew'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
