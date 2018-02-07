# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/auth"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def checkmobileexist(session, baseurl, mobile):
    """
    检查手机号是否已被注册
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "checkmobileexist"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def checkmobilenotexist(session, baseurl, mobile):
    """
    检查手机号没有被注册
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "checkmobilenotexist"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def login(session, baseurl, login, password, captcha, captchaId, bindShop=None, machineCode=None):
    """
    登录
    :param session:
    :param baseurl:
    :param login:
    :param password:
    :param captcha:
    :param captchaId:
    :param bindShop:
    :param machineCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login"
    ocurl = curl(url, session).method('post').headers(headers).params(login=login, password=password, captcha=captcha,
                                                                      captchaId=captchaId)
    if bindShop:
        ocurl.params(bindShop=bindShop)
    if machineCode:
        ocurl.params(machineCode=machineCode)
    return ocurl.perform()


def login_thirdparty(session, baseurl, body):
    """
    第三方登录QQ或微信
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login/thirdParty"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def login_thirdparty_appId_get(session, baseurl, authorizedBy):
    """
    获取app相关配置信息
    :param session:
    :param baseurl:
    :param authorizedBy: 授权方： QQ、WEIXIN等
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login/thirdParty"
    return curl(url, session).method('post').headers(headers).params(authorizedBy=authorizedBy).perform()


def password_reset(session, baseurl, login, password, authCode):
    """
    重置密码
    :param session:
    :param baseurl:
    :param login:
    :param password:
    :param authCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "password/reset"
    return curl(url, session).method('post').headers(headers).params(login=login, password=password,
                                                                     authCode=authCode).perform()


def register(session, baseurl, authCode, body):
    """
    用户注册
    :param session:
    :param baseurl:
    :param authCode: 手机校验码
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "register"
    return curl(url, session).method('post').headers(headers).params(authCode=authCode).body(body).perform()


def user_3rdParty_bind(session, baseurl, body):
    """
    第三方绑定千帆掌柜用户
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "user/thirdParty/bind"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def user_3rdParty_query(session, baseurl, id):
    """
    查询第三方登陆用户
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "user/thirdParty/query"
    return curl(url, session).method('post').headers(headers).params(id=id).perform()


def user_3rdParty_unbind(session, baseurl, id):
    """
    解绑第三方登陆用户
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "user/thirdParty/unbind"
    return curl(url, session).method('post').headers(headers).params(id=id).perform()

def version(session,baseurl):
    """
    获取版本号
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "version"
    return curl(url,session).headers(headers).perform()
