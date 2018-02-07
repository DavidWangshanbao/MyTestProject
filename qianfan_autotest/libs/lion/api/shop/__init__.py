# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/shop"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def appInfo(session, baseurl, shopId, machineCode):
    """
    获取门店基本信息
    :param session:
    :param baseurl:
    :param shopId:
    :param machineCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'appInfo'
    return curl(url, session).headers(headers).params(shopId=shopId, machineCode=machineCode).perform()


def create(session, baseurl, body):
    """
    新增门店, 不需要传shopConfig
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'create'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def create_before(session, baseurl):
    """
    检查门店限制数
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'create/before'
    return curl(url, session).method('post').headers(headers).perform()


def get(session, baseurl, shopId):
    """
    根据ID查询门店
    :param session:
    :param baseurl:
    :param shopId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(shopId=shopId).perform()


def invite_byuser(session, baseurl, mobile):
    """
    查询用户邀请中的门店
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get/invite/byuser'
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def getLogo(session, baseurl, body):
    """
    获取门店LOGO
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getLogo'
    return curl(url, session).headers(headers).body(body).perform()


def getServiceProvider(session, baseurl, uuid):
    """
    根据ID获取服务商
    :param session:
    :param baseurl:
    :param uuid: 服务商ID
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getServiceProvider'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getbyowner(session, baseurl, user, mobile):
    """
    查询用户自己的门店
    :param session:
    :param baseurl:
    :param user:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getbyowner'
    return curl(url, session).headers(headers).params(user=user, mobile=mobile).perform()


def getbysuppliermobile(session, baseurl, mobile):
    """
    根据手机查询供应商门店列表
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getbysuppliermobile'
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def getbyuser(session, baseurl, mobile, joinedOnly=None):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getbyuser'
    ocurl = curl(url, session).headers(headers).params(mobile=mobile)
    if joinedOnly:
        ocurl.params(joinedOnly=joinedOnly)
    return ocurl.perform()


def invite_accept(session, baseurl, shopId, joinCode, mobile):
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
    ocurl = curl(url, session).method('post').headers(headers)
    ocurl.params(shopId=shopId, joinCode=joinCode, mobile=mobile)
    return ocurl.perform()


def invite_refuse(session, baseurl, shopId, mobile):
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
    return curl(url, session).headers(headers).method('post').params(shopId=shopId, mobile=mobile).perform()


def joincode_update(session, baseurl, shop, version, joinCode):
    """
    修改入店码
    :param session:
    :param baseurl:
    :param shop:
    :param version:
    :param joinCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'joincode/update'
    return curl(url, session).headers(headers).params(shop=shop, version=version, joinCode=joinCode).perform()


def update(session, baseurl, body):
    """
    更新门店, 不需要传shopConfig
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'update'
    return curl(url, session).method('post').headers(headers).body(body).perform()
