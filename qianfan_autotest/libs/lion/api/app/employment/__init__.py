# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/employment"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getbyshop(session, baseurl, shopId, body):
    """
    获取门店除店主外的所有店员
    :param session:
    :param baseurl:
    :param shopId:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getbyshop'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId).body(body).perform()


def accept(session, baseurl, shopId, joinCode, mobile):
    """
    接受邀请
    :param session:
    :param baseurl:
    :param shopId:
    :param joinCode:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'invite/accept'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId, mobile=mobile,
                                                                     joinCode=joinCode).perform()


def refuse(session, baseurl, shopId, mobile):
    """
    拒绝邀请
    :param session:
    :param baseurl:
    :param shopId:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'invite/refuse'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId, mobile=mobile).perform()


def inviteagain(session, baseurl, shopId, mobile):
    """
    重新邀请店员，会发送短信
    :param session:
    :param baseurl:
    :param shopId:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'inviteagain'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId, mobile=mobile).perform()


def invitecount_byuser(session, baseurl, mobile):
    """
    获取用户邀请中的门店数量
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'invitecount/byuser'
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def qty_validate(session, baseurl, shop):
    """
    邀请店员前， 检查数量限制
    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'qty/validate'
    return curl(url, session).method('post').headers(headers).params(shop=shop).perform()


def remove(session, baseurl, id):
    """
    删除店员信息
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'remove'
    return curl(url, session).method('post').headers(headers).params(id=id).perform()


def save(session, baseurl, sendMsg, body):
    """
    邀请/修改店员
    :param session:
    :param baseurl:
    :param sendMsg: bool
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'save'
    return curl(url, session).method('post').headers(headers).params(sendMsg=session).body(body).perform()
