# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/v2/auth"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def login(session, baseurl, mobile, password):
    """
    登录
    :param session:
    :param baseurl:
    :param mobile:
    :param password:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login"
    return curl(url, session).method('post').headers(headers).params(mobile=mobile, password=password).perform()


def register(session, baseurl, body):
    """
    用户注册
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "register"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def sms_send(session, baseurl, mobile, exist):
    """
    发送短信
    :param session:
    :param baseurl:
    :param mobile:
    :param exist:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login"
    return curl(url, session).method('post').headers(headers).params(mobile=mobile, exist=exist).perform()
