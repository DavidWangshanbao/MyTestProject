# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/upowerPay"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def open_channels(session, baseurl, shop, body):
    """
    扫码支付方式开通
    :param session:
    :param baseurl:
    :param shop:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "channels/open"
    return curl(url, session).method('post').headers(headers).params(shop=shop).body(body).perform()


def query_test(session, baseurl, shop, payment, tranId, orderNumber):
    """
    支付测试结果查询,用于支付中情况
    :param session:
    :param baseurl:
    :param shop:
    :param payment:
    :param tranId:
    :param orderNumber:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query/test"
    return curl(url, session).headers(headers).params(shop=shop, payment=payment, tranId=tranId,
                                                      orderNumber=orderNumber).perform()


def submit_test(session, baseurl, shop, payCode, payment, tranId, orderNumber, machineCode=None, posNo=None):
    """
    开通支付后的支付测试
    :param session:
    :param baseurl:
    :param shop:
    :param payCode:
    :param payment:
    :param tranId:
    :param orderNumber:
    :param machineCode:
    :param posNo:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "submit/test"
    ocurl = curl(url, session).method('post').headers(headers).params(shop=shop, payment=payment, payCode=payCode,
                                                                      tranId=tranId, orderNumber=orderNumber)
    if machineCode:
        ocurl.params(machineCode=machineCode)
    if posNo:
        ocurl.params(posNo=posNo)
    return ocurl.perform()

def apply_weixin(session, baseurl, marchineCode, shopId, shopName, body):
    """
    微信开通申请,传入申请资料到易维工单，人工处理
    :param session:
    :param baseurl:
    :param marchineCode:
    :param shopId:
    :param shopName:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "weixin/apply"
    return curl(url,session).method('post').headers(headers).params(marchineCode=marchineCode,shopId=shopId,shopName=shopName).body(body).perform()