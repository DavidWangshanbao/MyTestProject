# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, uuid, activityType):
    """
    微信分享券活动查询
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param activityType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid, version=activityType).perform()


def drop(session, baseurl, tenant, uuid, version):
    """
    微信分享券活动下架
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/drop".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def publish(session, baseurl, tenant, uuid, version):
    """
    微信分享券活动发布
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/publish".format(tenant=tenant)
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
    url = _baseurl + "{tenant}/couponPublishingActivity/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, tenant, uuid, version, templateType):
    """
    微信分享券活动删除(物理删除)
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :param templateType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/remove".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version,
                                                                     templateType=templateType).perform()


def saveAndPublish(session, baseurl, tenant, body):
    """
    微信分享券活动保存并发布，支持新增并提交以及修改并发布
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/saveAndPublish".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, tenant, body):
    """
    微信分享券活动修改
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/saveModify".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveNew(session, baseurl, tenant, body):
    """
    微信分享券活动新增
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/couponPublishingActivity/saveNew".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
