# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "stack"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create(baseurl, app, requestid, size):
    """
    分配资源栈
    :param baseurl:
    :param app:
    :param requestid:
    :param size:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "create"
    return curl(url).method('post').headers(headers).params(requestid=requestid, size=size, app=app).perform()


def get_by_requestId(baseurl, app, requestid):
    """
    根据requestId获取资源栈信息
    :param baseurl:
    :param app:
    :param requestid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/{app}/{requestid}".format(app=app, requestid=requestid)
    return curl(url).headers(headers).perform()


def getById(baseurl, app, id):
    """
    根据id获取资源栈信息
    :param baseurl:
    :param app:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/{app}/{id}".format(app=app, id=id)
    return curl(url).headers(headers).params()


def get_by_apps_requestIds(baseurl, apps, requestids):
    """
    根据app和requestId批量获取资源栈信息源栈信息
    :param baseurl:
    :param apps:
    :param requestids:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "gets/by_apps_requestids"
    return curl(url).headers(headers).params(apps=apps, requestids=requestids).perform()


def get_by_requestIds(baseurl, app, requestids):
    """
根据requestId批量获取资源栈信息
    :param baseurl:
    :param app:
    :param requestids:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "gets/by_requestids/{app}".format(app=app)
    return curl(url).headers(headers).params(requestids=requestids).perform()
