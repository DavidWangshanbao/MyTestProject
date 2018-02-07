# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def issue(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/issue".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def batch_issue(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/batch_issue".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def consume(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/consume".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def single_consume(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/single_consume".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def batch_consume(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/batch_consume".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def rollback(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/rollback".format(tenant=tenant)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def get(session, baseurl, tenant, uuid, couponType, rsFetchParts):
    url = _get_prefix(baseurl) + "{tenant}/coupon/uuid_{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).headers(headers).params(couponType=couponType, rsFetchParts=rsFetchParts).perform()


def getByCode(session, baseurl, tenant, codeNs, codeId, couponType, rsFetchParts):
    url = _get_prefix(baseurl) + "{tenant}/coupon/code_ns_{code_ns}/code_id_{code_id}".format(tenant=tenant,
                                                                                              code_ns=codeNs,
                                                                                              code_id=codeId)
    return curl(url, session).headers(headers).params(couponType=couponType, rsFetchParts=rsFetchParts).perform()


def list(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/by_uuids".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def listByCodes(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/by_codes".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def occupy(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/occupy".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def release(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/release".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def getByCode(session, baseurl, tenant, code, couponType, rsFetchParts):
    url = _get_prefix(baseurl) + "{tenant}/coupon/code_id_{code_id}".format(tenant=tenant, code_id=code)
    return curl(url, session).headers(headers).params(couponType=couponType, rsFetchParts=rsFetchParts).perform()


def getValid(session, baseurl, tenant, uuid, couponType, rsFetchParts):
    url = _get_prefix(baseurl) + "{tenant}/coupon/valid/uuid_{uuid}".format(tenant=tenant, uuid=uuid)
    return curl(url, session).headers(headers).params(couponType=couponType, rsFetchParts=rsFetchParts).perform()


def listValid(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/valid/by_uuids".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def getValidByCode(session, baseurl, tenant, code, couponType, rsFetchParts):
    url = _get_prefix(baseurl) + "{tenant}/coupon/valid/code_id_{code_id}".format(tenant=tenant, code_id=code)
    return curl(url, session).headers(headers).params(couponType=couponType, rsFetchParts=rsFetchParts).perform()


def getValidByCode_nsid(session, baseurl, tenant, codeNs, codeId, couponType, rsFetchParts):
    url = _get_prefix(baseurl) + "{tenant}/coupon/valid/code_ns_{code_ns}/code_id_{code_id}".format(tenant=tenant,
                                                                                                    code_id=codeId,
                                                                                                    code_ns=codeNs)
    return curl(url, session).headers(headers).params(couponType=couponType, rsFetchParts=rsFetchParts).perform()


def listValidByCodes(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/valid/by_codes".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def changeOwner(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/change_owner".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def changePeriod(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/change_period".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def abort(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/abort".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def recover(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/coupon/recover".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
