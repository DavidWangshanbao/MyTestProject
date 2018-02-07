# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc, uuid):
    """
    获取我的组织
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/myorganization/get'.format(bloc=bloc)
    return curl(url, session).params(uuid=uuid).headers(headers).perform()


def save(session, baseurl, bloc, body):
    """
    获取我的组织
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/myorganization/save'.format(bloc=bloc)
    return curl(url, session).method('post').body(body).headers(headers).perform()
