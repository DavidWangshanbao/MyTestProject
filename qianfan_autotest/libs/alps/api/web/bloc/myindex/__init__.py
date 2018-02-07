# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc, userUuid, orgUuid):
    """
    获取自定义首页
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param userUuid: 用户uuid
    :param orgUuid: 组织uuid
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/myindex/get'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(userUuid=userUuid, orgUuid=orgUuid).perform()


def save(session, baseurl, bloc, body):
    """
    保存自定义首页
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/myindex/save'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
