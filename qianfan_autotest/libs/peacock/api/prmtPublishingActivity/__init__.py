# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def drop(session, baseurl, tenant, uuid, activity_type):
    """
    下架
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param activity_type:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/prmtPublishingActivity/drop'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, activity_type=activity_type).perform()


def get(session, baseurl, tenant, uuid, activityType):
    """
    分享促销活动查询
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param activityType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/prmtPublishingActivity/get'.format(tenant=tenant)
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
    url = _baseurl + '{tenant}/prmtPublishingActivity/publish'.format(tenant=tenant)
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
    url = _baseurl + '{tenant}/prmtPublishingActivity/query'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveAndPublish(session, baseurl, tenant, body):
    """
    分享促销活动保存并发布，支持新增并发布以及修改并发布
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/prmtPublishingActivity/saveAndPublish'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, tenant, body):
    """
    分享促销活动修改
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/prmtPublishingActivity/saveModify'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveNew(session, baseurl, tenant, body):
    """
    分享促销活动新增
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/prmtPublishingActivity/saveNew'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
