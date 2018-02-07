# coding=utf-8
"""
广告配置
"""
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/article'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def drop(session,baseurl,id,version):
    """
    下架文章
    :param session:
    :param baseurl:
    :param id:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "drop"
    return curl(url,session).method('post').headers(headers).params(id=id).params(version=version).perform()



def get(session,baseurl):
    """
    根据ID查找文章
    :param session:
    :param baseurl:
    :param id:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).method('post').headers(headers).params(id=id).params(version=version).perform()

def publish(session,baseurl,bArticle):
    """
    发布文章
    :param session:
    :param baseurl:
    :param bArticle:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "publish"
    return curl(url,session).headers(headers).method('post').body(bArticle).perform()

def query(session,baseurl,body):
    """
    查询文章
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url,session).method('post').headers(headers).body(body).perform()
