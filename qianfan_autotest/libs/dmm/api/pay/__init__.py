# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = 'web/web'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def pay(session, baseurl, accountId, req):
    """
    账户支付验证
    :param session:
    :param baseurl:
    :param accountId:
    :param req: (RequestBody)  PayRequest
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'accounts/{accountId}/pay'.format(accountId=accountId)
    return curl(url, session).method('post').headers(headers).body(req).perform()


def query(session, baseurl, accountId, shop, transId):
    """
    查询支付验证结果
    :param session:
    :param baseurl:
    :param accountId:
    :param shop:
    :param transId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'accounts/{accountId}/pay'.format(accountId=accountId)
    return curl(url, session).params(shop=shop, transId=transId).headers(headers).perform()
