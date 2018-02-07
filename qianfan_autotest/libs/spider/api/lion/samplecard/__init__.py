# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant):
    """
    查询卡样
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def get_qrcode(session, baseurl, tenant, card):
    """
    二维码预览查询
    :param session:
    :param baseurl:
    :param tenant:
    :param card:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/get/qrcode/{card}".format(tenant=tenant, card=card)
    return curl(url, session).headers(headers).perform()


def modify(session, baseurl, tenant, body):
    """
    修改卡样
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/save/modify".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def new(session, baseurl, tenant, body):
    """
    新建卡样
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/save/new".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def upload_logo(session, baseurl, tenant, afile):
    """
    logo上传
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/upload/logo".format(tenant=tenant)
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').perform(files=files)


def logo_flag(session, baseurl, tenant):
    """
    获取用于手机上传的flag
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/upload/logo/flag".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def logo_result(session, baseurl, tenant, flag, afile):
    """
    logo手机上传,flag将用于查询结果
    :param session:
    :param baseurl:
    :param tenant:
    :param flag:
    :param afile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/upload/logo/result".format(tenant=tenant)
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').params(flag=flag).perform(files=files)


def logo_result_flag(session, baseurl, tenant, flag):
    """
    logo手机上传,flag将用于查询结果
    :param session:
    :param baseurl:
    :param tenant:
    :param flag:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/lion/samplecard/upload/logo/result/{flag}".format(tenant=tenant, flag=flag)
    return curl(url, session).headers(headers).perform()
