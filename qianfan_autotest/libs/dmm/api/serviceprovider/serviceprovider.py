# coding=utf-8
from __future__ import unicode_literals, print_function
import json
from utils import baseurl_strip, curl

PREFIX = "web/web/serviceprovider"

headers = {
    'content-type': 'application/json;charset=utf-8'
}


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, uuid):
    """
    服务商详情
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).params(uuid=uuid).headers(headers).perform(timeout=5)


def query(session, baseurl, body):
    """
    查询服务商列表
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url,session).headers(headers).method('post').body(body).perform()


def export(session, baseurl, body):
    """
    下载符合条件的服务商列表文件
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'export'
    return curl(url, session).method('post').headers(headers).body(body).perform(timeout=5)


def assign_list(session, baseurl, deviceId):
    """
    待分配的设备
    :param session:
    :param baseurl:
    :param deviceId: 设备编号
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'assign/list'
    if deviceId:
        return curl(url,session).headers(headers).params(deviceId= deviceId).perform(timeout=5)
    else:
        return curl(url,session).headers(headers).perform(timeout=5)

def assign(session, baseurl, targetid, deviceUuids):
    """
    分配
    :param session:
    :param baseurl:
    :param targetid: 分配目标
    :param deviceUuids: (RequestBody) List<String>
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'assign/{targetid}'.format(targetid=targetid)

    # return session.post(url, timeout=5, headers=headers, \
    #                     data=json.dumps(deviceUuids, ensure_ascii=False).encode('utf-8'))
    return curl(url,session).method('post').headers(headers).body(deviceUuids).perform()

def editPassword(session, baseurl,bpassword):
    """
    修改密码
    :param session:
    :param baseurl:
    :param bpassword: BPassword-like python dict
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'editPassword'
    return curl(url,session).method('post').headers(headers).body(bpassword).perform(timeout=5)

