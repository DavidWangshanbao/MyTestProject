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
    disable付款方式
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytype/disable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()

def enable(session, baseurl, bloc, uuid, version):
    """
    enable付款方式
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytype/enable'.format(bloc=bloc)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()

def query(session, baseurl, bloc, body):
    """
    enable付款方式
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytype/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()

def savemodify(session, baseurl, bloc, body,version):
    """
    修改付款方式
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytype/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).params(version=version).perform()

def savenew(session, baseurl, bloc, body):
    """
    创建付款方式
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/paytype/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()