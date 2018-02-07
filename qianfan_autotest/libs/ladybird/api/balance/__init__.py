# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "service/1/points-balance"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getByAccount(session, baseurl, tenant, account):
    url = _get_prefix(baseurl) + "get-points-account"
    return curl(url, session).headers(headers).params(account=account, tenant=tenant).perform()


def getOverduePoints(session, baseurl, tenant, account, days):
    url = _get_prefix(baseurl) + "get-overduepoints-account"
    return curl(url, session).headers(headers).params(account=account, tenant=tenant, days=days).perform()


def getOverdueOwner(session, baseurl, tenant, days, ownerId, ownerNamespace, providerId, providerNamespace):
    url = _get_prefix(baseurl) + "/get-overduepoints-owner/{ownerid},{ownerns},{providerid},{providerns}" \
        .format(ownerid=ownerId, ownerns=ownerNamespace, providerid=providerId, providerns=providerNamespace)
    return curl(url, session).headers(headers).params(days=days, tenant=tenant).perform()


def listByAccount(session, baseurl, tenant, accounts):
    url = _get_prefix(baseurl) + 'list-points-account'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(accounts).perform()


def getByOwner(session, baseurl, tenant, ownerId, ownerNamespace, providerId, providerNamespace):
    url = _get_prefix(baseurl) + '/get-points-owner/{ownerid},{ownerns}'.format(ownerid=ownerId, ownerns=ownerNamespace)
    params = {
        "provider-id": providerId,
        "provider-ns": providerNamespace
    }
    return curl(url, session).headers(headers).params(params).perform()


def listByOwners(session, baseurl, tenant, ownerId, ownerNamespace, providerId, providerNamespace):
    url = _get_prefix(baseurl) + '/list-points-owner/{ownerid},{ownerns}'.format(ownerid=ownerId,
                                                                                 ownerns=ownerNamespace)
    params = {
        "provider-id": providerId,
        "provider-ns": providerNamespace
    }
    return curl(url, session).method('post').headers(headers).params(params).perform()


def getDetailByOwner(session, baseurl, tenant, ownerId, ownerNamespace):
    url = _get_prefix(baseurl) + '/get-detailpoints-owner/{ownerid},{ownerns}'.format(ownerid=ownerId,
                                                                                      ownerns=ownerNamespace)
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def listDetailsByOwners(session, baseurl, tenant, ownerNamespace, ownerIds):
    url = _get_prefix(baseurl) + '/list-detailspoints-owner/{ownerns}'.format(ownerns=ownerNamespace)
    curl(url, session).method('post').headers(headers).params(tenant=tenant).body(ownerIds).perform()


def getByTeant(session, baseurl, tenant):
    url = _get_prefix(baseurl) + 'get-points-tenant'
    return curl(url, session).headers(headers).params(tenant=tenant).perform()


def sum(session, baseurl, tenant,qc):
    url = _get_prefix(baseurl) + 'sum'
    return curl(url, session).method('post').headers(headers).params(tenant=tenant).body(qc).perform()
