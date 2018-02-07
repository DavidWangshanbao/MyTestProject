# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def saveNew(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/save_new".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def saveModify(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/save_modify".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def enable(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/enable".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def disable(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/disable".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def get(session, baseurl, tenant, uuid, issueType):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).headers(headers).params(issueType=issueType).perform()


def list(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/by_uuids".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def getRemainingCount(session, baseurl, tenant, uuid):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/remaining_count/uuid_{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).headers(headers).perform()


def listRemainingCounts(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/list_remaining_count".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def getReceivableCount(session, baseurl, tenant, uuid, ownerNamespace, ownerId):
    url = _get_prefix(
        baseurl) + "{tenant}/coupon_issue/receivable_count/uuid_{uuid}/owner_na_{owner_na}/owner_id_{owner_id}" \
              .format(tenant=tenant, uuid=uuid, owner_na=ownerNamespace, owner_id=ownerId)
    return curl(url, session).headers(headers).perform()


def listReceivableCounts(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon_issue/list_receivable_count".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
