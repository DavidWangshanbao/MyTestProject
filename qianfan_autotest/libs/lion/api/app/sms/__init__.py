# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/sms"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check(session, baseurl, mobile, code):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "check"
    return curl(url, session).method('post').headers(headers).params(mobile=mobile, code=code).perform()


def send(session, baseurl, mobile):
    """
    smsVerificationCode
    :param session:
    :param baseurl:
    :param mobile: 手机号
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "send"
    return curl(url, session).method('post').headers(headers).params(mobile=mobile).perform()
