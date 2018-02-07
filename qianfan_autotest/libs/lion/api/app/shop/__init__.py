# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/shop"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, shop):
    """
    修根据uuid获取门店
    :param session:
    :param baseurl:
    :param shop:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url, session).headers(headers).params(shop=shop).perform()


def get_by_owner(session, baseurl, user, mobile):
    """

    :param session:
    :param baseurl:
    :param user:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/byOwner"
    return curl(url, session).headers(headers).params(user=user, mobile=mobile).perform()


def get_by_supplier_mobile(session, baseurl, mobile):
    """

    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/bySupplierMobile"
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def get_by_user(session, baseurl, joinedOnly, mobile):
    """

    :param session:
    :param baseurl:
    :param joinedOnly: boolean
    :param mobile: string
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get/byUser"
    return curl(url, session).headers(headers).params(joinedOnly=joinedOnly, mobile=mobile).perform()


def joincode_update(session, baseurl, shop, version, joinCode):
    """
    修改门店入店码
    :param session:
    :param baseurl:
    :param shop:
    :param version:
    :param joinCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "joincode/update"
    return curl(url, session).method('post').headers(headers) \
        .params(shop=shop, version=version, joinCode=joinCode).perform()


def open_validate(session, baseurl, user):
    """

    :param session:
    :param baseurl:
    :param user:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "open/validate"
    return curl(url, session).method('post').headers(headers).params(user=user).perform()


def saveModify(session, baseurl, shop, license=None, banner=None):
    """
    修改保存门店信息
    :param session:
    :param baseurl:
    :param shop:
    :param license:
    :param banner:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "saveModify"
    ocurl = curl(url, session).method('post').headers(headers).params(shop=shop)
    if license:
        ocurl.params(license=license)
    if banner:
        ocurl.params(banner=banner)
    return ocurl.perform()


def saveNew(session, baseurl, shop, license=None, banner=None):
    """
    新增保存门店信息
    :param session:
    :param baseurl:
    :param shop:
    :param license:
    :param banner:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "saveNew"
    ocurl = curl(url, session).method('post').headers(headers).params(shop=shop)
    if license:
        ocurl.params(license=license)
    if banner:
        ocurl.params(banner=banner)
    return ocurl.perform()
