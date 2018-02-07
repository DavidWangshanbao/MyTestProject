# coding=utf-8
"""
广告配置
"""
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/adPutConfig'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def save_new(session, baseurl, body):
    """
    新增广告配置
    :param session:
    :param baseurl:
    :param body: (RequestBody) BAdPutConfig
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "saveNew"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def update(session, baseurl, body):
    """
    编辑广告配置
    :param session:
    :param baseurl:
    :param body: (RequestBody) BAdPutConfig
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "update"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, id):
    """
    删除广告配置
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "remove"
    return curl(url, session).headers(headers).params(id=id).perform()


def query(session, baseurl, request):
    """
    查询广告配置
    :param session:
    :param baseurl:
    :param request: (RequestBody) ListObjectRequest python like dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(request).perform()


def get(session, baseurl, id):
    """
    根据ID查找
    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(id=id).perform()
