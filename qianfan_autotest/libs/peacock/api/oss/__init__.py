# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def deleteById(session, baseurl, tenant, storage_id):
    """
    文件删除
    :param session:
    :param baseurl:
    :param tenant:
    :param storage_id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/oss/deleteById'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(storage_id=storage_id).perform()


def fileUpload(session, baseurl, tenant, body):
    """
    文件上传
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/oss/fileUpload'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def getFileById(session, baseurl, tenant, storage_id):
    """
    文件查询
    :param session:
    :param baseurl:
    :param tenant:
    :param storage_id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/oss/getFileById'.format(tenant=tenant)
    return curl(url, session).headers(headers).params(storage_id=storage_id).perform()


def upload(session, baseurl, tenant, files):
    """
    文件上传
    :param session:
    :param baseurl:
    :param tenant:
    :param files:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/oss/upload'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(files=files).perform()
