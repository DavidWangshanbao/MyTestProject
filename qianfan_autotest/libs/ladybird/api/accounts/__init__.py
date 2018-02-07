# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "service/1/points-accounts"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def open(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'open'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()


def unfreeze(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'unfreeze'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()


def obtain(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'obtain'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()


def use(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'use'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()


def adjust(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'adjust'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()


def rollback(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'rollback'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()


def getRequestState(session, baseurl, tenant, requestId):
    url = _get_prefix(baseurl) + 'request-state/{id}'.format(id=requestId)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def getRequestStateByTransnsid(session, baseurl, tenant, ns, id):
    url = _get_prefix(baseurl) + 'request-state/{ns},{id}'.format(id=id, ns=ns)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def getAccount(session, baseurl, tenant, uuid):
    url = _get_prefix(baseurl) + uuid
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def getAccount_byownerprovider(session, baseurl, tenant, ownerNs, ownerId, providerNs, providerId):
    url = _get_prefix(baseurl) + 'by-owner-provider'
    params = {
        "owner-ns": ownerNs,
        "owner-id": ownerId,
        "tenant": tenant,
        "provider-ns": providerNs,
        "provider-id": providerId
    }
    return curl(url, session).headers(headers).params(params).perform()


def listAccounts_byuuids(session, baseurl, tenant, uuids):
    url = _get_prefix(baseurl) + 'by-uuids'
    return curl(url, session).method('post').headers(headers).body(uuids).params(tenant=tenant).perform()


def listAccounts_byownersname(session, baseurl, tenant, ownerNs, providerNs, providerId, ownerIds):
    url = _get_prefix(baseurl) + 'by-owners-name'
    params = {
        'tenant': tenant,
        "owner-ns": ownerNs,
        "provider-ns": providerNs,
        "provider-id": providerId,
    }
    return curl(url, session).method('post').headers(headers).body(ownerIds).params(params).perform()


def getByOwner(session, baseurl, tenant, ownerNs, ownerId):
    url = _get_prefix(baseurl) + 'by-owner'
    params = {
        "tenant": tenant,
        "owner-ns": ownerNs,
        "owner-id": ownerId
    }
    return curl(url, session).headers(headers).params(params).perform()
