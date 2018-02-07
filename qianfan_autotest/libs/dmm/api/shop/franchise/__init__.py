# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/shop/franchise"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, body):
    """
    加盟店搜索
    :param session:
    :param baseurl:
    :param body: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def create(session, baseurl, body):
    """
    加盟店创建
    :param session:
    :param baseurl:
    :param body:(RequestBody) FranchiseShopRequest
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'create'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def cancel(session, baseurl, key):
    """
    加盟店取消加盟
    :param session:
    :param baseurl:
    :param key: (RequestBody) AccessKey
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'cancel'
    return curl(url, session).method('post').headers(headers).body(key).perform()


def get(session, baseurl, key):
    """
    通过accessKey获取DPOS门店信息
    :param session:
    :param baseurl:
    :param key: (RequestBody) AccessKey DPOS API 秘钥对象
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).method('post').headers(headers).body(key).perform()


def checkExternalShop(session, baseurl, externalShop):
    """
    校验服务商门店
    :param session:
    :param baseulr:
    :param externalShop: (String) 店铺别称
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'checkExternalShop'
    return curl(url, session).method('post').params(externalShop=externalShop).headers(headers).perform()


def modify(session, baseurl, body):
    """
    编辑/保存
    :param session:
    :param baseurl:
    :param body: (RequestBody) BServiceProviderShop
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'modify'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def dtl(session, baseurl, id):
    """
    获取详情
    :param session:
    :param baseurl:
    :param id: 关系表id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'dtl'
    return curl(url, session).headers(headers).params(id=id).perform()
