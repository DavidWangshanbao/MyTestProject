# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/employment"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check_code(session, baseurl, shop, code, uuid=None):
    """
    检查编号是否重复
    :param session:
    :param baseurl:
    :param shop:
    :param code:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "check/code"
    ocurl = curl(url, session).headers(headers).params(shop=shop, code=code)
    if uuid:
        ocurl.params(uuid=uuid)
    return ocurl.perform()


def create(session, baseurl, body, sendMsg=True):
    """
    新增邀请店员
    :param session:
    :param baseurl:
    :param body:
    :param sendMsg:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "create"
    return curl(url, session).method('post').headers(headers).params(sendMsg=sendMsg).body(body).perform()


def get_code(session, baseurl, shop):
    """
    查询最新可用编号
    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/code"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def getbyshop(session, baseurl, shopId, start, limit, _filter=None, _sort=None):
    """
    获取门店除店主外的所有店员
    :param session:
    :param baseurl:
    :param shopId:
    :param start:
    :param limit:
    :param _filter:
    :param _sort:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getbyshop"
    ocurl = curl(url, session).method('post').headers(headers).params(shopId=shopId, start=start, limit=limit)

    if _filter:
        ocurl.params(filter=_filter)
    if _sort:
        ocurl.params(sort=_sort)

    return ocurl.perform()


def invite_accept(session, baseurl, shopId, joinCode, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "invite/accept"
    return curl(url, session).headers(headers).params(shopId=shopId, joinCode=joinCode, mobile=mobile).perform()


def invite_refuse(session, baseurl, shopId, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "invite/refuse"
    return curl(url, session).headers(headers).params(shopId=shopId, mobile=mobile).perform()


def inviteagain(session, baseurl, shop, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "inviteagain"
    return curl(url, session).headers(headers).params(shop=shop, mobile=mobile).perform()


def invitecount_byuser(session, baseurl, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "invitecount/byuser"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()

def qty_validate(session, baseurl, shop):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "qty/validate"
    return curl(url, session).headers(headers).params(shop=shop).perform()

def remove(session, baseurl, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "remove"
    return curl(url, session).headers(headers).params(id=id).perform()

def update(session, baseurl, body,sendMsg=True):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "update"
    return curl(url, session).headers(headers).params(sendMsg=sendMsg).body(body).perform()
