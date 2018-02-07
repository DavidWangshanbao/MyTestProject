# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


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
    url = _baseurl + '{tenant}/smsPushCouponActivity/drop'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def get(session, baseurl, tenant, uuid):
    """
    短信发送券活动查询
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/smsPushCouponActivity/get'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


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
    url = _baseurl + '{tenant}/smsPushCouponActivity/publish'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def remove(session, baseurl, tenant, uuid, version, templateType=None):
    """
     短信发送券活动删除(物理删除)
    :param session:
    :param baseurl:
    :param tenant:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/smsPushCouponActivity/publish'.format(tenant=tenant)
    ocurl = curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version)
    if templateType:
        ocurl.params(templateType=templateType)
    return ocurl.perform()


def saveAndPublish(session, baseurl, tenant, body):
    """
    短信发送券活动保存并发布，支持新增并提交以及修改并发布
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/smsPushCouponActivity/saveAndPublish'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, tenant, body):
    """
    短信发送券活动修改
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/smsPushCouponActivity/saveModify'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveNew(session, baseurl, tenant, body):
    """
    短信发送券活动新增
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/smsPushCouponActivity/saveNew'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
