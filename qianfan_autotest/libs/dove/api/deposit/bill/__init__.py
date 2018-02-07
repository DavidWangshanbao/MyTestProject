# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def saveNew(session,baseurl,tenant,body):
    url=_get_prefix(baseurl)+'{tenant}/depositbill/saveNew'.format(tenant=tenant)
    return curl(url,session).method('post').body(body).perform()


def saveModify(session,baseurl,tenant,body):
    url=_get_prefix(baseurl)+'{tenant}/depositbill/saveModify'.format(tenant=tenant)
    return curl(url,session).method('post').body(body).perform()

def confirm(session,baseurl,tenant,body):
    url=_get_prefix(baseurl)+'{tenant}/depositbill/confirm'.format(tenant=tenant)
    return curl(url,session).method('post').body(body).perform()

def cancel(session,baseurl,tenant,body):
    url=_get_prefix(baseurl)+'{tenant}/depositbill/cancel'.format(tenant=tenant)
    return curl(url,session).method('post').body(body).perform()

def get(session,baseurl,tenant,uuid):
    url = _get_prefix(baseurl) + '{tenant}/depositbill/get'.format(tenant=tenant)
    return curl(url,session).headers(headers).params(uuid=uuid).perform()

def list(session,baseurl,tenant,uuids):
    url=_get_prefix(baseurl)+'{tenant}/depositbill/list'.format(tenant=tenant)
    return curl(url,session).method('post').body(uuids).perform()


def query(session, baseurl, tenant, body):
    url=_get_prefix(baseurl)+'{tenant}/depositbill/query'.format(tenant=tenant)
    return curl(url,session).method('post').body(body).perform()
