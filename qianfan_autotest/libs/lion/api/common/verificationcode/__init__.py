# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/common/verificationcode"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def fetch(session, baseurl, uuid):
    """
    获取图片验证码
    :param session:
    :param baseurl:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'fetch'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def sms(session, baseurl, mobile):
    """
    发送短信验证码
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'sms'
    return curl(url, session).method('post').headers(headers).params(mobile=mobile).perform()
