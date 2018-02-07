# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/shop/pay"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def cancel(session,baseurl,shop,channelPayRenewType,renew):
    _baseurl= _get_prefix(baseurl)
    url = _baseurl+"cancel/{}".format(shop)
    return curl(url,session).method('post').params(channelPayRenewType=channelPayRenewType,renew=renew).perform()

def check(session, baseurl, shop, tranIds):
    _baseurl= _get_prefix(baseurl)
    url = _baseurl+"check/{}".format(shop)
    return curl(url,session).method('post').params(channelPayRenewType=tranIds).perform()


def create(session,baseurl,shop,channelPayRenewType,renew):
    _baseurl= _get_prefix(baseurl)
    url = _baseurl+"create/{shop}".format(shop  =shop)
    return curl(url,session).method('post').params(channelPayRenewType=channelPayRenewType,renew=renew).perform()

def payItem(session,baseurl,shop,channelPayRenewType,renew):
    _baseurl= _get_prefix(baseurl)
    url = _baseurl+"payItem/{shop}".format(shop=shop)
    return curl(url,session).method('post').params(channelPayRenewType=channelPayRenewType,renew=renew).perform()