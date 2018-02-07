# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/auth"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def login(session, baseurl, mobile, password, bindShop=None):
    """
    登录系统
    :param session:
    :param baseurl:
    :param mobile:
    :param password:
    :param bindShop: (Optional)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login"
    ocurl = curl(url, session).method('post').headers(headers).params(mobile=mobile, password=password)
    if bindShop:
        ocurl.params(bindShop=bindShop)
    return ocurl.perform()


def mobilenotexist(session, baseurl, mobile):
    """
    手机号已被注册时校验失败
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "mobilenotexist/check"
    return curl(url, session).method('post').headers(headers).params(mobile=mobile).perform()


def register(session, baseurl, authCode, body):
    """
    用户注册
    :param session:
    :param baseurl:
    :param authCode:手机校验码
    :param body:用户信息
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "register"
    return curl(url, session).method('post').headers(headers).params(authCode=authCode).body(body).perform()
