# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = 'web/web/common/verificationcode'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def fetch(session, baseurl, uuid):
    """
    发送验证码
    :param session:
    :param baseurl:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'fetch'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def sms(session, baseurl, uuid):
    """
    发送短信
    :param session:
    :param baseurl:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'sms'
    return curl(url, session).headers(headers).params(uuid=uuid).params()
