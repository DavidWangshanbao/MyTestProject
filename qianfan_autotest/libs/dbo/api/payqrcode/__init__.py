# coding=utf-8
"""
广告配置
"""
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/web/shop/payqrcode'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def batchQrCode(session, baseurl, uuids):
    """
    批量获取下载收款码
    :param session:
    :param baseurl:
    :param uuids: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "batchQrCode"
    return curl(url, session).method('post').headers(headers).body(uuids).perform()


def downloadQrcode(session, baseurl, uuid):
    """
    下载收款码图片
    :param session:
    :param baseurl:
    :param uuid: (String)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'downloadQrcode'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getQrCode(session, baseurl, uuid):
    """
    获取收款码信息
    :param session:
    :param baseurl:
    :param uuid: (String)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getQrCode'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def qrCodeUrl(session, baseurl, uuid):
    """
    获取收款码地址
    :param session:
    :param baseurl:
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'qrCodeUrl'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()
