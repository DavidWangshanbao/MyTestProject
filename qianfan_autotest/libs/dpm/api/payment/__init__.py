# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pay"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl

def insurance(session,baseurl,payMode,page,pageSize):
    """
    查询保单明细列表
    :param session:
    :param baseurl:
    :param payMode:
    :param page:
    :param pageSize:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url= _baseurl + "insurance"
    return curl(url,session).method('post').headers(headers).params(page=page,payMode=payMode,pageSize=pageSize).perform()

def ofbank(session,baseurl,payMode,bankAccount):
    """
    根据账户获取账户支付信息
    :param session:
    :param baseurl:
    :param payMode:
    :param bankAccount:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "ofbank"
    return curl(url, session).method('post').headers(headers).params(payMode=payMode).body(bankAccount).perform()

def pay(session,baseurl,payment):
    """
    导入账户信息
    :param session:
    :param baseurl:
    :param payment:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "pay"
    return curl(url, session).method('post').headers(headers).body(payment).perform()

def queryaccounts(session,baseurl,convert):
    """

    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "queryaccounts"
    return curl(url, session).method('post').headers(headers).body(convert).perform()