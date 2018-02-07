# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = 'web/web/shop/qrcode'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getQrCode(session, baseurl, uuid):
    """
    获取收款码信息
    :param session:
    :param baseurl:
    :param uuid: 门店id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getQrCode'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def qrCodeUrl(session, baseurl, uuid):
    """
    获取收款码链接
    :param session:
    :param baseurl:
    :param uuid: 门店id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'qrCodeUrl'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def downloadQrcode(session, baseurl, uuid):
    """
    下载收款码图片
    :param session:
    :param baseurl:
    :param uuid: 门店id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'downloadQrcode'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def batchQrCode(session, baseurl, body):
    """
    批量获取下载收款码
    :param session:
    :param baseurl:
    :param body: (RequestBody) List<String> like python list
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'batchQrCode'
    return curl(url, session).method('post').headers(headers).body(body).perform()
