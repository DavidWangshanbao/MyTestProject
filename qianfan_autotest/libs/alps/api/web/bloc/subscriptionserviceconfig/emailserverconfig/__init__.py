# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc):
    """
    获取邮件服务配置
    :param session:
    :param baseurl:
    :param bloc:集团
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptionserviceconfig/emailserverconfig/get'.format(bloc=bloc)
    return curl(url, session).headers(headers).perform()


def savemodify(session, baseurl, bloc, body):
    """
    修改邮件服务配置
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptionserviceconfig/emailserverconfig/savemodify'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, body):
    """
    新建邮件服务配置
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptionserviceconfig/emailserverconfig/savenew'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def sendemailtest(session, baseurl, bloc, emailAddress, body):
    """
    发送邮件测试
    :param session:
    :param baseurl:
    :param emailAddress:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptionserviceconfig/emailserverconfig/sendemailtest'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(emailAddress=emailAddress).body(body).perform()
