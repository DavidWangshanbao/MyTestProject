# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, tenant, day):
    url = _get_prefix(baseurl) + "{tenant}/account_day_report/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(day=day).perform()


def query(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/account_day_report/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
