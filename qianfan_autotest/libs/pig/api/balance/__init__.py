# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/prepay-web/1/balance"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getByAccount(session, baseurl, tenant, account):
    url = _get_prefix(baseurl) + 'by-account'
    return curl(url, session).headers(headers).params(tenant=tenant, account=account).perform()


def getByOwner(session, baseurl, tenant, ownerNS, ownerId, name='default'):
    url = _get_prefix(baseurl) + 'by-owner/{ns},{id}'.format(ns=ownerNS, id=ownerId)
    return curl(url, session).headers(headers).params(tenant=tenant, name=name).perform()


def listByAccounts(session, baseurl, tenant, accounts):
    url = _get_prefix(baseurl) + 'by-accounts'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(accounts).perform()


def listByOwner(session, baseurl, tenant, ownerNamespace, ownerIds, name='default'):
    url = _get_prefix(baseurl) + 'by-owner-ids/{ns}'.format(ns=ownerNamespace)
    return curl(url, session).method('post').headers(headers).params(tenant=tenant, name=name).body(ownerIds).perform()


def getByTenant(session, baseurl, tenant):
    url = _get_prefix(baseurl) + 'by-tenant'
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def sum(session, baseurl, tenant, qc):
    url = _get_prefix(baseurl) + 'sum'
    return curl(url, session).method('post').params(tenant=tenant).body(qc).perform()


def getDetailByOwner(session, baseurl, tenant, ownerNS, ownerId):
    url = _get_prefix(baseurl) + 'account-name-by-owner-id/{ns},{id}'.format(ns=ownerNS, id=ownerId)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def listDetailsByOwners(session, baseurl, tenant, ownerNS, body):
    url = _get_prefix(baseurl) + 'account-name-by-owner-ids/{ns}'.format(ns=ownerNS)
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()
