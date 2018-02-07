# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/shop/config"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def accesskey_reset(session, baseurl, shop, targetShop, mobile, authCode):
    """

    :param session:
    :param baseurl:
    :param shop:
    :param targetShop:
    :param mobile:
    :param authCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'accessKey/reset'
    return curl(url, session).headers(headers).params(shop=shop, authCode=authCode, mobile=mobile,
                                                      targetShop=targetShop).perform()


def get(session, baseurl, shop):
    """

    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(shop=shop).perform()


def get_by_owner(session, baseurl, user):
    """

    :param session:
    :param baseurl:
    :param user:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get/byOwner'
    return curl(url, session).headers(headers).params(user=user).perform()


def saleTagTpl_update(session, baseurl, shop, version, saleTagTpl):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'saleTagTpl/update'
    return curl(url, session).method('post').headers(headers).params(shop=shop, version=version,
                                                                     saleTagTpl=saleTagTpl).perform()


def save(session, baseurl, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'save'
    return curl(url, session).method('post').body(body).perform()
