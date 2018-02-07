# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/payBox"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def basechannel_bank(session, baseurl, body):
    """
    查询银行(固定按银行代码正序排序)

    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/bank"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def basechannel_branch(session, baseurl, body):
    """
    查询支行(固定按银行代码正序排序)

    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/branch"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def basechannel_get(session, baseurl, user):
    """
    获取用户的基础开户资料
    :param session:
    :param baseurl:
    :param user:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/get"
    return curl(url, session).headers(headers).params(user=user).perform()


def basechannel_industry(session, baseurl, body):
    """
    获取行业信息 role:可空，为空时：查询所有实体类型，不为空时查询条件实体类型下的所有经营分类 category:可空（和role关联操作，role为空category一定为空，role不为空category可空），role不为空category为空时：查询当前role下的所有经营分类，不为空时查询当前role下的category下的所有经营范围
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/industry"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def basechannel_open(session, baseurl, body):
    """
    开通基础通道
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/open"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def basechannel_region(session, baseurl, province, city):
    """
    查询地址，查省时，所有参数为空
    :param session:
    :param baseurl:
    :param province:
    :param city:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/region"
    return curl(url, session).headers(headers).params(province=province, city=city).perform()


def payments(session, baseurl, channel):
    """

    :param session:
    :param baseurl:
    :param channel:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "channel/payments"
    return curl(url, session).headers(headers).params(channel=channel).perform()


def delete(session, baseurl, id, smsCode):
    """
    删除盒子
    :param session:
    :param baseurl:
    :param id:
    :param smsCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "delete"
    return curl(url, session).headers(headers).params(id=id, smsCode=smsCode).perform()


def get(session, baseurl, owner, deviceId, shopId):
    """
    获取绑定信息
    :param session:
    :param baseurl:
    :param owner:
    :param deviceId:
    :param shopId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(owner=owner, shopId=shopId, deviceId=deviceId).perform()


def list(session, baseurl, user):
    """
    列出店主所有的盒子
    :param session:
    :param baseurl:
    :param user:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "list"
    return curl(url, session).headers(headers).params(user=user).perform()


def save(session, baseurl, body):
    """
    修改盒子
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "save"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def shop_list(session, baseurl, mobile):
    """
    查询用户已加入的所有门店
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "shop/list"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()
