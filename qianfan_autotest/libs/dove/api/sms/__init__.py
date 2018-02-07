# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def send(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/send".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def batch_send(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/batch_send".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def preview(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/preview".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def success(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/success".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def fail(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/fail".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get(session, baseurl, tenant, uuid):
    url = _get_prefix(baseurl) + "{tenant}/sms/get".format(tenant=tenant)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def list(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/list".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query(session, baseurl, tenant, body):
    url = _get_prefix(baseurl) + "{tenant}/sms/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()
