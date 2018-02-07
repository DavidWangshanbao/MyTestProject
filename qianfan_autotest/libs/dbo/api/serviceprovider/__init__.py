# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/web/serviceprovider"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def assign(session, baseurl, service_provider_id, afile):
    """
    Python requests 上传文件参见： http://docs.python-requests.org/en/master/user/quickstart/#post-a-multipart-encoded-file
    :param session:
    :param baseurl:
    :param service_provider_id: 服务商id
    :param afile: 上传文件路径
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'assign'
    params = {
        "serviceProviderId": service_provider_id
    }
    files = {'file': open(afile, 'rb')}
    return session.post(url, timeout=5, params=params, files=files)


def export(session, baseurl, req):
    """
    导出服务商列表
    :param session:
    :param baseurl:
    :param req:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'export'
    return curl(url, session).method('post').headers(headers).body(req).perform()


def get(session, baseurl, uuid):
    """
    服务商详情
    :param session:
    :param baseurl:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, req):
    """
    服务商列表
    :param session:
    :param baseurl:
    :param req:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).method('post').headers(headers).body(req).perform()


def qeryLevelOne(session, baseurl):
    """
    一级服务商列表
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'qeryLevelOne'
    return curl(url, session).headers(headers).perform()


def saveModify(session, baseurl, body):
    """
    编辑服务商
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'saveModify'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveNew(session, baseurl, body):
    """
    新建服务商
    :param session:
    :param baseurl:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'saveNew'
    return curl(url, session).method('post').headers(headers).body(body).perform()
