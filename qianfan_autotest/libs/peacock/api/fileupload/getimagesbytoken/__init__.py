# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).headers(headers).perform()


def delete(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).method('delete').headers(headers).perform()


def head(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).method('head').headers(headers).perform()


def options(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).method('options').headers(headers).perform()


def patch(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).method('patch').headers(headers).perform()


def post(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).method('post').headers(headers).perform()


def put(session, baseurl, tenant, token):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/fileUpload/getImagesByToken/{token}".format(tenant=tenant, token=token)
    return curl(url, session).method('put').headers(headers).perform()
