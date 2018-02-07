# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def send(session, baseurl, tenant, mobile):
    """
    发送短信验证码
    :param session:
    :param baseurl:
    :param tenant:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/sms/send".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(mobile=mobile).perform()


def validate(session, baseurl, tenant, mobile, captcha):
    """
    验证短信验证码
    :param session:
    :param baseurl:
    :param tenant:
    :param mobile:
    :param captcha:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/sms/validate".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(mobile=mobile, captcha=captcha).perform()
