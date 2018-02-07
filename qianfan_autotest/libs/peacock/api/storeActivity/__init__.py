# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getActivity(session, baseurl, tenant, organizer):
    """
    查询当前生效的微信分享券活动
    :param session:
    :param baseurl:
    :param tenant:
    :param organizer: 活动组织者ID
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/getActivity/{organizer}'.format(tenant=tenant, organizer=organizer)
    return curl(url, session).headers(headers).perform()


def getById(session, baseurl, tenant, storeId):
    """
    根据门店标识查询门店信息
    :param session:
    :param baseurl:
    :param tenant:
    :param storeId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/getById'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(storeId=storeId).perform()


def getQRCodeState(session, baseurl, tenant, storeId):
    """
    查询是否在收银小票上打印二维码
    :param session:
    :param baseurl:
    :param tenant:
    :param storeId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/getQRCodeState'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(storeId=storeId).perform()


def modifyQRCodeState(session, baseurl, tenant, storeId, state):
    """
    查询是否在收银小票上打印二维码
    :param session:
    :param baseurl:
    :param tenant:
    :param storeId:
    :param state:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/modifyQRCodeState'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(storeId=storeId, state=state).perform()


def query_sku_bybarcode(session, baseurl, tenant, store, barcode):
    """
    精确查询门店商品信息（根据Barcode）
    :param session:
    :param baseurl:
    :param tenant:
    :param store:
    :param barcode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/{store}/query/sku/bybarcode'.format(tenant=tenant, store=store)
    return curl(url, session).headers(headers).params(barcode=barcode).perform()


def querySkus(session, baseurl, tenant, store, body):
    """
    查询不同条件商品明细：商品ID不为空则仅根据商品ID查询，否则根据商品标签、商品名称、非值查询明细
    :param session:
    :param baseurl:
    :param tenant:
    :param store:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/{store}/querySkus'.format(tenant=tenant, store=store)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def queryTags(session, baseurl, tenant, store):
    """
    获取门店所有商品标签
    :param session:
    :param baseurl:
    :param tenant:
    :param store:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/{store}/queryTags'.format(tenant=tenant, store=store)
    return curl(url, session).headers(headers).perform()


def updatesku(session, baseurl, tenant, store, body):
    """
    编辑商品资料
    :param session:
    :param baseurl:
    :param tenant:
    :param store:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/storeActivity/{store}/update/sku'.format(tenant=tenant, store=store)
    return curl(url, session).method('post').headers(headers).body(body).perform()
