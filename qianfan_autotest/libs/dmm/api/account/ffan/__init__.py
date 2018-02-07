# coding=utf-8
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/accounts"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def post(session, baseurl, body):
    """
    添加支付账户(飞凡通)
    :param session:
    :param baseurl:
    :param body: (RequestBody) HashMap
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'ffan'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def put(session, baseurl, body):
    """
        添加支付账户(飞凡通)
        :param session:
        :param baseurl:
        :param body: (RequestBody) HashMap
        :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'ffan'
    return curl(url, session).method('put').headers(headers).body(body).perform()
