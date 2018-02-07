# coding=utf-8
"""
文章管理
"""
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 'article'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def publish(session, baseurl, bArticle):
    """
    发布文章
    :param session:
    :param baseurl:
    :param bArticle: (RequestBody) BArticle python like dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "publish"
    return curl(url, session).method('post').headers(headers).body(bArticle).perform()


def drop(session, baseurl, id, version):
    """
    下架文章
    :param session:
    :param baseurl:
    :param id:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "operate/drop"
    return curl(url, session).method('post').headers(headers).params(id=id, version=version).perform()


def get(session, baseurl, id, version):
    """
    根据ID查找文章
    :param session:
    :param baseurl:
    :param id:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "operate/get"
    return curl(url, session).method('post').headers(headers).params(id=id, version=version).perform()


def query(session, baseurl, body):
    """
    查询文章
    :param session:
    :param baseurl:
    :param body: (RequestBody) ListObjectRequest python like dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "operate/query"
    return curl(url, session).method('post').headers(headers).body(body).perform()
