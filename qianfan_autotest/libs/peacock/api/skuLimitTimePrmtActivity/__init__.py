# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def conflictCheck(session, baseurl, tenant, body):
    """
    商品限时促销活动内容冲突校验
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/conflictCheck'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def drop(session, baseurl, tenant, uuid, version):
    """
    下架
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/drop'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def get(session, baseurl, tenant, uuid, activityType):
    """
    商品限时促销活动查询
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param activityType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/get'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid, activityType=activityType).perform()


def publish(session, baseurl, tenant, uuid, version):
    """
    发布
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/publish'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def query(session, baseurl, tenant, body):
    """
    分页批量查询
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/query'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def querySkuPromotionOrder(session, baseurl, tenant, organize, activityType, body):
    """
    商品促销活动 订单 销售统计详细
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param activityType:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/querySkuPromotionOrder'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organize=organize, activityType=activityType).body(
        body).perform()


def querySkuPromotionOrderSum(session, baseurl, tenant, organize, activityType, body):
    """
    商品促销活动 订单 销售总计
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param activityType:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/querySkuPromotionOrderSum'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organize=organize, activityType=activityType).body(
        body).perform()


def querySkuPromotionSku(session, baseurl, tenant, organize, activityType, body):
    """
    商品促销活动 商品 销售统计报表
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param activityType:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/querySkuPromotionSku'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organize=organize, activityType=activityType).body(
        body).perform()


def queryTopics(session, baseurl, tenant, organize, topic=None, activity=None):
    """
    商品限时促销活动主题查询
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param topic: 活动主题
    :param activity: 活动标识
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/queryTopics'.format(tenant=tenant)
    ocurl = curl(url, session).headers(headers).params(organize=organize)
    if topic:
        ocurl.params(topic=topic)
    if activity:
        ocurl.params(activity=activity)
    return ocurl.perform()


def remove(session, baseurl, tenant, uuid, version):
    """
    商品限时促销活动删除(物理删除)
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/remove'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def saveAndPublish(session, baseurl, tenant, body):
    """
    商品限时促销活动保存并发布，支持新增并发布以及修改并发布
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/saveAndPublish'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, tenant, body):
    """
    商品限时促销活动修改
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/saveModify'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).params()


def saveNew(session, baseurl, tenant, body):
    """
    商品限时促销活动新增
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/skuLimitTimePrmtActivity/saveNew'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).params()
