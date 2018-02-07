# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def request(session, baseurl, tenant, shop, body):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/request/{shop}".format(tenant=tenant, shop=shop)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def abandon(session, baseurl, tenant, uuid, body):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/abandon/{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def allow(session, baseurl, tenant, uuid, body):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/allow/{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def disAllow(session, baseurl, tenant, uuid, body):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/disAllow/{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get(session, baseurl, tenant, uuid):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/get/{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).headers(headers).perform()


def list(session, baseurl, tenant, uuids):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/list".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(uuids).perform()


def getLastByShop(session, baseurl, tenant, shop):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/getLastByShop/{shop}".format(tenant=tenant, shop=shop)
    return curl(url, session).headers(headers).perform()


def listLastsByShops(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/signRequisition/listLastsByShops".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
