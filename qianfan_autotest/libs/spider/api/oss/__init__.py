# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl

def delete_by_id(session,baseurl,tenant,storage_id):
    """
    文件删除
    :param session:
    :param baseurl:
    :param tenant:
    :param storage_id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/oss/delete_by_id".format(tenant=tenant)
    return curl(url,session).method('post').headers(headers).params(storage_id=storage_id).perform()

def file_upload(session,baseurl,tenant,body):
    """
    文件上传
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/oss/file_upload".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()

def get_file_by_id(session,baseurl,tenant,storage_id):
    """
    文件查询
    :param session:
    :param baseurl:
    :param tenant:
    :param storage_id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/oss/get_file_by_id".format(tenant=tenant)
    return curl(url, session).headers(headers).params(storage_id=storage_id).perform()

def upload(session,baseurl,tenant,files):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/oss/upload".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(files=files).perform()