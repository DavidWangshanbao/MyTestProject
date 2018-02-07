# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/user"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, id):
    """
    根据uuid获取用户信息
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(id=id).perform()


def mobile_update(session, baseurl, user, mobile, authCode):
    """
    修改手机号
    :param session:
    :param baseurl:
    :param user:
    :param mobile:
    :param authCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "mobile/update"
    return curl(url, session).method('post').headers(headers).params(user=user, mobile=mobile,
                                                                     authCode=authCode).perform()


def mobile_notexist_check(session, baseurl, mobile):
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


def password_reset(session, baseurl, mobile, password, authCode):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "password/reset"
    return curl(url, session).method('post').headers(headers).params(mobile=mobile, password=password,
                                                                     authCode=authCode).perform()


def payment_get(session, baseurl, id):
    """
    根据uuid获取用户支付方式信息
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "payment/get"
    return curl(url, session).headers(headers).params(id=id).perform()


def phote_change(session, baseurl, userId, images):
    """
    修改保存用户头像信息
    :param session:
    :param baseurl:
    :param userId:
    :param images:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "photo/change"
    return curl(url, session).method('post').headers(headers).params(userId=userId, images=images).perform()


def photos_default(session, baseurl):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "photos/default"
    return curl(url, session).headers(headers).perform()


def refundPwd_check(session, baseurl, id, password):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "refundPwd/check"
    return curl(url, session).headers(headers).params(id=id, password=password).perform()


def refundPwd_reset(session, baseurl, id, password):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "refundPwd/reset"
    return curl(url, session).headers(headers).params(id=id, password=password).perform()


def saveModify(session, baseurl, user, images=None):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "saveModify"
    ocurl = curl(url, session).method('post').headers(headers).params(user=user)
    if images:
        ocurl.params(images=images)

    return ocurl.perform()
