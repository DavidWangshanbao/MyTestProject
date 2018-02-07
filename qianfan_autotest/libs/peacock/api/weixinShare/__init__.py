# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def downloadPoster(session, baseurl, tenant, body):
    """
    下载微信分享活动海报
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/weixinShare/downloadPoster'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def generatePoster(session, baseurl, tenant, body):
    """
    生成微信分享活动海报
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/weixinShare/generatePoster'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def generateQrCodeUrl(session, baseurl, tenant, body):
    """
    生成微信分享二维码
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/weixinShare/generateQrCodeUrl'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def preview(session, baseurl, tenant):
    """
    预览店铺橱窗
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/weixinShare/preview'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).perform()
