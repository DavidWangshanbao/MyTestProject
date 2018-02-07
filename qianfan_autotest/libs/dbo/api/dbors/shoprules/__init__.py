# coding=utf-8
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 'rules/shop'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create_shop_rule(baseurl, auth, body):
    """
    新增门店规则
    :param baseurl:
    :param auth:
    :param body:
    :return:
    """
    url = _get_prefix(baseurl)
    return curl(url).headers(headers).method('post').body(body).perform(auth=auth)


def delete_cache(baseurl, auth):
    """
    清除缓存
    :param baseulr:
    :param auth:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "deleteCache"
    return curl(url).method('delete').headers(headers).perform(aut=auth)


def delete_shop_rule(baseurl, auth, uuid, version=None):
    """

    :param baseurl:
    :param auth:
    :param uuid: 门店uuid
    :param version: 门店规则版本号，非必填
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + uuid
    curl_obj = curl(url).method('delete').headers(headers)
    if version:
        curl_obj.params(version=version)

    curl_obj.perform(auth=auth)


def get(baseurl, auth, uuid):
    """
    查询有效的门店规则
    :param baseurl:
    :param auth:
    :param uuid: 门店uuid
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + uuid
    return curl(url).headers(headers).perform(auth=auth)


def modify_shop_rule(baseurl, auth, uuid, body, version=None):
    """
    修改门店规则
    :param baseurl:
    :param auth:
    :param uuid: 门店uuid
    :param body: 要修改的门店规则
    :param version: 门店规则版本号，非必填
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + uuid
    ocurl = curl(url).headers(headers).method('put').body(body)
    if version:
        ocurl.params(version=version)
    return ocurl.params(auth=auth)
