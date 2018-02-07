# coding=utf-8
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/ad'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def export(session, baseurl, afilter):
    """
    开始导出
    :param session:
    :param baseurl:
    :param afilter:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "export"
    return curl(url, session).headers(headers).params(filter=afilter).perform()


def stop(session, baseurl):
    """
    停止导出
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "stop"
    return curl(url, session).headers(headers).perform()


def get_progress(session, baseurl):
    """
    获取进度
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "getProgress"
    return curl(url, session).headers(headers).perform()


def check_job(session, baseurl):
    """
    检查进度
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "checkJob"
    return curl(url, session).headers(headers).perform()


def save_newAd(session, baseurl, bAd):
    """
    新增广告创意
    :param session:
    :param baseurl:
    :param bAd: (RequestBody) BAd python like dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "saveNewAd"
    return curl(url, session).method('post').headers(headers).body(bAd).perform()


def modify_ad(session, baseurl, bAd):
    """
    编辑广告创意
    :param session:
    :param baseurl:
    :param bAd: (RequestBody) BAd python like dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "modifyAd"
    return curl(url, session).method('post').headers(headers).body(bAd).perform()


def query(session, baseurl, body):
    """
    查询广告创意
    :param session:
    :param baseurl:
    :param body: (RequestBody) ListObjectRequest
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).method('post').headers(headers).body(body).perform()


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
