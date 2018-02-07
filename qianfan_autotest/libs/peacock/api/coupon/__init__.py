# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check(session, baseurl, tenant, organizer, couponCode):
    """
    验券
    :param session:
    :param baseurl:
    :param tenant:
    :param organizer:
    :param couponCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/check".format(tenant=tenant)
    return curl(url, session).headers(headers).params(organizer=organizer, couponCode=couponCode).perform()


def consume(session, baseurl, tenant, organizer, couponCode, tranNo):
    """
    券核销
    :param session:
    :param baseurl:
    :param tenant:
    :param organizer:
    :param couponCode:
    :param tranNo:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/consume".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organizer=organizer, couponCode=couponCode,
                                                                     tranNo=tranNo).perform()


def queryActivityDataLines(session, baseurl, tenant, organize, activityType):
    """
    券核销
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param activityType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/queryActivityDataLines".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organize=organize,
                                                                     activityType=activityType).perform()


def queryActivityReport(session, baseurl, tenant, organize, activityType):
    """
    券统计报表数据总览查询
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param activityType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/queryActivityReport".format(tenant=tenant)
    return curl(url, session).headers(headers).params(organize=organize, activityType=activityType).perform()


def queryActivityTrendLines(session, baseurl, tenant, organize, activityType):
    """
    券统计报表数据明细查询
    :param session:
    :param baseurl:
    :param tenant:
    :param organize:
    :param activityType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/queryActivityTrendLines".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).params(organize=organize,
                                                                     activityType=activityType).perform()


def queryCouponRecord(session, baseurl, tenant, body):
    """
    券操作记录查询
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/coupon/queryCouponRecord".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
