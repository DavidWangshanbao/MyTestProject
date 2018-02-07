# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/user"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def checkmobilenotexist(session, baseurl, mobile):
    """
    检查手机号没有被注册,手机号已被注册时抛出业务异常
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "checkmobilenotexist"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def defaultPhotos(session, baseurl):
    """
    获取系统默认的几张默认头像
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "defaultPhotos"
    return curl(url, session).headers(headers).perform()


def editMobile(session, baseurl, id, version, mobile, oldMobile, oldAuthCode, authCode):
    """
    修改手机号
    :param session:
    :param baseurl:
    :param id:
    :param version:
    :param mobile:
    :param oldMobile:
    :param oldAuthCode:
    :param authCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "editMobile"
    return curl(url, session).method('post').headers(headers).params(id=id, version=version, mobile=mobile) \
        .params(oldMobile=oldMobile, oldAuthCode=oldAuthCode, authCode=authCode).perform()


def get(session, baseurl, id):
    """
    获取用户基本信息
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(id=id).perform()


def logout(session, baseurl):
    """
    注销
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "logout"
    return curl(url, session).method('post').perform()


def get_paymentInfo(session, baseurl, id):
    """
    获取用户信息，包括扫码支付开通信息
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "paymentInfo/get"
    return curl(url, session).headers(headers).params(id=id).perform()


def user_update(session, baseurl, user, images):
    """
    修改保存个人信息
    :param session:
    :param baseurl:
    :param user:
    :param images:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "user/update"
    return curl(url, session).method('post').headers(headers).params(user=user, images=images).perform()
