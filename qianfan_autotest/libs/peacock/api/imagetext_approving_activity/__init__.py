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
    图文活动查询
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/get'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def preview(session, baseurl, tenant, uuid):
    """
    图文活动预览
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/preview'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def publish2ShowWindow(session, baseurl, tenant, uuid, rversion, guideImage):
    """
发布到店铺橱窗
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param rversion:
    :param guideImage:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/publish2ShowWindow'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, rversion=rversion,
                                                                     guideImage=guideImage).perform()


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
    url = _baseurl + '{tenant}/imagetext_approving_activity/query'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, tenant, uuid):
    """
    图文活动删除(物理删除)
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/query'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid).perform()


def save_and_submit(session, baseurl, tenant, body):
    """
    图文活动保存并提交，支持新增并提交以及修改并提交
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/save_and_submit'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def save_modify(session, baseurl, tenant, body):
    """
    图文活动修改
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/save_modify'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def save_new(session, baseurl, tenant, body):
    """
    图文活动新增
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/save_new'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def submit(session, baseurl, tenant, uuid, version):
    """
    提交审批
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/imagetext_approving_activity/submit'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()
