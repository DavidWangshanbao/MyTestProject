# coding=utf-8
import json
from utils import baseurl_strip, headers, curl

PREFIX = "web/web/merchant"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check(session, baseurl, mobile):
    """
    检查是否开户或在开户中,success=true:开户或在开户中, success=false:可开户
    :param session:
    :param baseurl:
    :param mobile: 手机号码
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "check"
    return curl(url, session).headers(headers).method('post').params(mobile=mobile).perform()


def add(session, baseurl, body):
    """
    开户
    :param session:
    :param baseurl:
    :param body: (RequestBody) AMerchant
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "add"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def modify(session, baseurl, body):
    """
    编辑
    :param session:
    :param baseurl:
    :param body: (RequestBody) AMerchant
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "mod"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def dtl(session, baseurl, id):
    """
    获取用户的基础开户资料
    :param session:
    :param baseurl:
    :param id: 商户id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "dtl"
    return curl(url, session).headers(headers).params(id=id).perform()


def list(session, baseurl, body):
    """
    查询开户列表
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'list'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def export(session, baseurl, body):
    """
    下载符合条件的开户商户列表文件
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'export'
    return curl(url, session).method('post').headers(headers).body(body).perform()
