# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/pos"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create(session, baseurl, shopId, body):
    """
    绑定
    :param session:
    :param baseurl:
    :param shopId:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'create'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId).body(body).perform()


def getbyshop(session, baseurl, shopId, _filter=None, _sort=None):
    """
    获取门店的所有pos机
    :param session:
    :param baseurl:
    :param shopId:
    :param _filter:
    :param _sort:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getbyshop'
    ocurl = curl(url, session).headers(headers).params(shopId=shopId)
    if _filter:
        ocurl.params(filter=_filter)
    if _sort:
        ocurl.params(sort=_sort)
    return ocurl.perform()


def list(session, baseurl, shopId):
    """
    获取门店的所有pos机
    :param session:
    :param baseurl:
    :param shopId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'list'
    return curl(url, session).headers(headers).params(shopId=shopId).perform()


def remove(session, baseurl, shopId, id):
    """
    解绑
    :param session:
    :param baseurl:
    :param shopId:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'remove'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId, id=id).perform()


def remove_by_no(session, baseurl, shopId, posNo):
    """
    解绑
    :param session:
    :param baseurl:
    :param shopId:
    :param posNo:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'remove/byno'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId, posNo=posNo).perform()


def update(session, baseurl, shopId, body):
    """
    编辑
    :param session:
    :param baseurl:
    :param shopId:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'update'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId).body(body).perform()
