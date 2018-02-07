# coding=utf-8
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 'rules/user'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create_urser_rule(baseurl, auth, body):
    """
    新增用户规则
    :param baseurl:
    :param auth: (username,password) turple
    :param body: (ResponseBody)
    :return:
    """
    url = _get_prefix(baseurl)
    return curl(url, ).method('post').headers(headers).body(body).perform(auth=auth)


def delete_cache(baseurl, auth):
    """
    清除UserRules缓存
    :param baseurl:
    :param auth: (username,password) turple
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "deleteCache"
    return curl(url).method('delete').headers(headers).perform(auth=auth)


def delete_user_rule(baseurl, auth, uuid):
    """
    删除用户规则
    :param baseurl:
    :param auth: (username,password) turple
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + uuid
    return curl(url).method("delete").headers(headers).perform(auth=auth)


def get_user_rule(baseurl, auth, uuid):
    """
    查询有效用户规则
    :param baseurl:
    :param auth:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + uuid
    return curl(url).headers(headers).perform(auth=auth)


def modify_user_rule(baseurl, auth, uuid, body, version=None):
    """
    修改用户规则
    :param baseurl:
    :param auth:
    :param uuid: 用户uuid
    :param body:
    :param version:(Optional) 用户规则版本号
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + uuid
    curl_obj = curl(url).method('put').headers(headers).body(body)
    if version:
        curl_obj.params(version=version)

    return curl_obj.perform(auth=auth)


