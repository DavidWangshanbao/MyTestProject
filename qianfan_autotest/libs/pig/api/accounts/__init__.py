# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/prepay-web/1/prepay-accounts"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def openBatchly(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "open-batchly"
    return curl(url, session).method('post').headers((headers)).params(tenant=tenant).body(body).perform()


def freeze(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "freeze"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def unfreeze(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "unfreeze"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def freezeBatchly(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "freeze-batchly"
    return curl(url, session).method('post').headers((headers)).params(tenant=tenant).body(body).perform()


def unfreezeBatchly(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "unfreeze-batchly"
    return curl(url, session).method('post').headers((headers)).params(tenant=tenant).body(body).perform()


def deposit(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "deposit"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def depositBatchly(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "deposit-batchly"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def pay(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "pay"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def adjust(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "adjust"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def rollback(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "rollback"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def refund(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "refund"
    return curl(url, session).method('put').headers((headers)).params(tenant=tenant).body(body).perform()


def getRequestState(session, baseurl, tenant, requestId):
    url = _get_prefix(baseurl) + "request-state/{requestid}".format(requestid=requestId)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def getRequestState_nsid(session, baseurl, tenant, transNs, transId):
    url = _get_prefix(baseurl) + "request-state/{transns},{transid}".format(transns=transNs, transid=transId)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def get(session, baseurl, uuid):
    url = _get_prefix(baseurl) + uuid
    return curl(url, session).headers(headers).perform()


def get_by_owner_name(session, baseurl, tenant, ownerNs, ownerId, name='default'):
    url = _get_prefix(baseurl) + 'by-owner-name'
    params = {
        "tenant": tenant,
        "owner-ns": ownerNs,
        "owner-id": ownerId,
        'name': name
    }
    return curl(url, session).headers(headers).params(params).perform()


def list_by_uuids(session, baseurl, tenant, uuids):
    url = _get_prefix(baseurl) + 'by-uuids'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(uuids).perform()


def list_by_owners_name(session, baseurl, tenant, ownerNs, ownerIds, name='default'):
    url = _get_prefix(baseurl) + 'by-owners-name'
    params = {
        'tenant': tenant,
        'owner-ns': ownerNs,
        'name': name
    }
    return curl(url, session).method('post').headers(headers).params(params).body(ownerIds).perform()


def getByOwner(session, baseurl, tenant, ownerNs, ownerId):
    url = _get_prefix(baseurl) + 'by-owner'
    params = {
        'tenant': tenant,
        'owner-ns': ownerNs,
        'owner-id': ownerId
    }
    return curl(url, session).headers(headers).params(params).perform()


def changeOwner(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + 'change-owner'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(body).perform()
