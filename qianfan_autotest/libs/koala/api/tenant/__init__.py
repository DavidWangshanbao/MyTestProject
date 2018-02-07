# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/tenant"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def disable(session, baseurl, uuid, version, string):
    url = _get_prefix(baseurl) + '_disable'
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version,
                                                                     string=string).perform()


def enable(session, baseurl, uuid, version, string):
    url = _get_prefix(baseurl) + '_enable'
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version,
                                                                     string=string).perform()


def get(session, baseurl, uuid):
    url = _get_prefix(baseurl) + '_get'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getByGatewayTenant(session, baseurl, gatewayTenant):
    url = _get_prefix(baseurl) + '_getByGatewayTenant'
    return curl(url, session).headers(headers).params(gatewayTenant=gatewayTenant).perform()


def getBySourceEntity(session, baseurl, body):
    url = _get_prefix(baseurl) + '_getBySourceEntity'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def getEnabled(session, baseurl, uuid):
    url = _get_prefix(baseurl) + '_getEnabled'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def list(session, baseurl, body):
    url = _get_prefix(baseurl) + '_list'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def listByGatewayTenants(session, baseurl, gatewayTenant):
    url = _get_prefix(baseurl) + '_listByGatewayTenants'
    return curl(url, session).method('post').headers(headers).params(gatewayTenant=gatewayTenant).perform()


def listBySourceEntities(session, baseurl, namespace, ids):
    url = _get_prefix(baseurl) + '_listBySourceEntities'
    return curl(url, session).method('post').headers(headers).params(namespace=namespace).body(ids).perform()


def listEnabled(session, baseurl, body):
    url = _get_prefix(baseurl) + '_listEnabled'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query(session, baseurl, body):
    url = _get_prefix(baseurl) + '_query'
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, string, body):
    url = _get_prefix(baseurl) + '_saveModify'
    return curl(url, session).method('post').headers(headers).params(string=string).body(body).perform()


def saveNew(session, baseurl, string, body):
    url = _get_prefix(baseurl) + '_saveNew'
    return curl(url, session).method('post').headers(headers).params(string=string).body(body).perform()
