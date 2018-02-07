# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def takePicture(session, baseurl, tenant, type):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/fileUpload/takePicture/{type}'.format(tenant=tenant, type=type)
    return curl(url, session).headers(headers).perform()


def uploadImage(session, baseurl, tenant, type, files):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/fileUpload/uploadImage/{type}'.format(tenant=tenant, type=type)
    return curl(url, session).method('post').headers(headers).params(files=files).perform()


def uploadImageToEweiWithToken(session, baseurl, tenant, token, files):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/fileUpload/uploadImageToEweiWithToken'.format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(token=token, files=files).perform()


def uploadImageWithToken(session, baseurl, tenant, type, token, files):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{tenant}/fileUpload/uploadImageWithToken/{type}'.format(tenant=tenant, type=type)
    return curl(url, session).method('post').headers(headers).params(token=token, files=files).perform()
