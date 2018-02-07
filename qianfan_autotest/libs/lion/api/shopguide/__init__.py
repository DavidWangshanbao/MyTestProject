# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/shopguide"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create(session, baseurl, body):
    """
    新增导购员
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'create'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get(session, baseurl, id, shopId):
    """
    根据uuid查找导购员
    :param session:
    :param baseurl:
    :param id:
    :param shopId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(id=id, shopId=shopId).perform()


def getByCode(session, baseurl, shopId, code):
    """
    根据编号查找导购员
    :param session:
    :param baseurl:
    :param shopId:
    :param code:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get/byCode'
    return curl(url, session).headers(headers).params(shopId=shopId, code=code).perform()


def list(session, baseurl, shopId, body):
    """
    获取门店所有导购员
    :param session:
    :param baseurl:
    :param shopId:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'list'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId).body(body).perform()


def query(session, baseurl, shopId, body):
    """
    此接口支持分页，带查询条件;若需要一次查询全部数据，则limit传0
    :param session:
    :param baseurl:
    :param shopId:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).headers(headers).method('post').params(shopId=shopId).body(body).perform()


def remove(session, baseurl, id, shopId):
    """
    删除导购员
    :param session:
    :param baseurl:
    :param id:
    :param shopId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'remove'
    return curl(url, session).headers(headers).params(id=id, shopId=shopId).perform()


def update(session, baseurl, body):
    """
    修改导购员信息
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'update'
    return curl(url, session).method('post').headers(headers).body(body).perform()
