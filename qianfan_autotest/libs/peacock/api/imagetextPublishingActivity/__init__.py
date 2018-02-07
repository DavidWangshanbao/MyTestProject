# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, uuid):
    """
    分享图文活动查询
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetextPublishingActivity/get'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


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
    url = _baseurl + '{tenant}/imagetextPublishingActivity/drop'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


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
    url = _baseurl + '{tenant}/imagetextPublishingActivity/publish'.format(tenant=tenant)
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
    url = _baseurl + '{tenant}/imagetextPublishingActivity/query'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, tenant, uuid, version):
    """
    分享图文活动删除(物理删除)
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetextPublishingActivity/remove'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def saveAndPublish(session, baseurl, tenant, body):
    """
    分享图文活动保存并提交，支持新增并发布以及修改并发布
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetextPublishingActivity/saveAndPublish'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, tenant, body):
    """
    分享图文活动修改
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetextPublishingActivity/saveModify'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveNew(session, baseurl, tenant, body):
    """
    分享图文活动新增
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetextPublishingActivity/saveNew'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
