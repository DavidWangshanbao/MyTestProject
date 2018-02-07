# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/session"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, shop, machineCode=None):
    """
    加载会话
    返回用户信息、门店信息、服务版本
    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    ocurl = curl(url, session).headers(headers).params(shop=shop)
    if machineCode:
        ocurl.params(machineCode=machineCode)

    return ocurl.perform()
