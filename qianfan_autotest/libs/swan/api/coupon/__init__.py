# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl

def queryActivity(session,baseurl,tenant,shop,memberId=None):
    """
    有效微信分享券活动
    :param session:
    :param baseurl:
    :param tenant:
    :param shop:
    :param memberId:
    :return:
    """
    _baseurl=_get_prefix(baseurl)
    url = _baseurl+ "{tenant}/coupon/queryActivity".format(tenant=tenant)
    ocurl= curl(url,session).headers(headers).params(shop=shop)
    if memberId:
        ocurl.params(memberId=memberId)
    return ocurl.perform()

def getTicketActivity(session,baseurl,tenant,shop,amount,memberId=None):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/getTicketActivity".format(tenant=tenant)
    ocurl = curl(url, session).headers(headers).params(shop=shop,amount=amount)
    if memberId:
        ocurl.params(memberId=memberId)
