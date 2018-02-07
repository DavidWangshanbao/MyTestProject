# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/serviceprovider/device"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def modify(session, baseurl, body):
    """

    :param session:
    :param baseurl:
    :param body: (RequestBody) BServiceProviderDeviceModify like python dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'modify'
    return curl(url, session).method('post').headers(headers).body(body).perform(timeout=5)


def get(session, baseurl, uuid):
    """
    设备详情
    :param session:
    :param baseurl:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(uuid=uuid).perform(timeout=5)


def query(session, baseurl, body):
    """
    设备列表
    :param session:
    :param baseurl:
    :param body:(RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).method("post").headers(headers).body(body).perform()


def export(session, baseurl, body):
    """
    导出设备列表
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'export'
    return curl(url, session).method('post').headers(headers).body(body).perform()
