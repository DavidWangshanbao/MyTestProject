# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def password(session, baseurl, tenant, body):
    """
    设置会员密码
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/credential/password".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def password_opened(session, baseurl, tenant, member):
    """
    查询会员是否开通支付密码
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/credential/password/opened".format(tenant=tenant)
    return curl(url, session).headers(headers).params(member=member).perform()


def sms_verify(session, baseurl, tenant, mobile):
    """
    短信验证
    :param session:
    :param baseurl:
    :param tenant:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/credential/sms/verify".format(tenant=tenant)
    return curl(url, session).headers(headers).params(mobile=mobile).perform()
