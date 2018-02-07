# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/upowerPay/aliPay"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def isvOpen_query(session, baseurl, xid, tenantId):
    """
    扫描二维码后，查询授权情况
    :param session:
    :param baseurl:
    :param xid: 授权id
    :param tenantId:商户id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "isvOpen/query"
    return curl(url, session).headers(headers).params(xid=xid, tenantId=tenantId).perform()


def get(session, baseurl):
    """
    获取口碑开店的二维码
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "isvOpen/get"
    return curl(url, session).headers(headers).perform()


def bind_shop(session, baseurl, shop, tenantId, aliPayShop, aliPayShopName, machineCode, posNo=None):
    """
    绑定口碑门店
    :param session:
    :param baseurl:
    :param shop:
    :param tenantId:
    :param aliPayShop:
    :param aliPayShopName:
    :param machineCode:
    :param posNo:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "shop/bind"
    ocurl = curl(url, session).method('post').headers(headers).params(shop=shop, tenantId=tenantId,
                                                                      aliPayShop=aliPayShop,
                                                                      aliPayShopName=aliPayShopName,
                                                                      machineCode=machineCode)
    if posNo:
        ocurl.params(posNo=posNo)
    return ocurl.perform()


def query_shop(session, baseurl, start, limit, shop=None):
    """
    查询商户绑定的口碑门店, success用于界面区别是没有开通扫码支付还是没有在口碑开店。如果返回false，什么都不处理
    :param session:
    :param baseurl:
    :param start:
    :param limit:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "shop/query"
    ocurl = curl(url, session).headers(headers).params(start=start, limit=limit)
    if shop:
        ocurl.params(shop=shop)
    return ocurl.perform()
