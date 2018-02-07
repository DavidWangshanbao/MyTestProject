# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/device"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def delete(session, baseurl, id, smsCode):
    """
    删除设备
    :param session:
    :param baseurl:
    :param id:
    :param smsCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "delete"
    return curl(url, session).headers(headers).params(id=id, smsCode=smsCode).perform()


def get(session, baseurl, deviceId, deviceType):
    """
    获取绑定信息
    :param session:
    :param baseurl:
    :param deviceId:
    :param deviceType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(deviceId=deviceId, deviceType=deviceType).perform()


def list(session, baseurl, user):
    """
    列出店主所有的设备
    :param session:
    :param baseurl:
    :param user:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "list"
    return curl(url, session).headers(headers).params(user=user).perform()


def save(session, baseurl, body):
    """
    修改设备
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "save"
    return curl(url, session).headers(headers).body(body).perform()
