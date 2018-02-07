# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "product"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, shop, ownerMobile):
    """
    取得所有允许在指定零售店销售的商品
    :param session:
    :param baseurl:
    :param shop:
    :param ownerMobile:
    :return:
    """
    url = _get_prefix(baseurl)
    return curl(url, session).headers(headers).params(shop=shop, ownerMobile=ownerMobile).perform()


def get_by_city(session, baseurl, shop, ownerMobile, city):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'city/{city}'.format(city=city)
    return curl(url, session).headers(headers).params(shop=shop, ownerMobile=ownerMobile).perform()


def get_by_productId(session, baseurl, productId, fetch_parts):
    """
    根据uuid取得产品
    :param session:
    :param baseurl:
    :param productId:
    :param fetch_parts:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + productId
    return curl(url, session).headers(headers).params(fetch_parts=fetch_parts).perform()
