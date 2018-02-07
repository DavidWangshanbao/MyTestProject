# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/route"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def delete(session, baseurl, uuid, version, s):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_delete'
    return curl(url, session).headers(headers).params(**{
        'uuid': uuid,
        'versin': version,
        "string": s
    }).perform()


def disable(session, baseurl, uuid, version, s):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_disable'
    return curl(url, session).headers(headers).params(**{
        'uuid': uuid,
        'versin': version,
        "string": s
    }).perform()


def get(session, baseurl, uuid, fetchParts):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_get'
    return curl(url, session).headers(headers).params(uuid=uuid, fetchParts=fetchParts).perform()


def getByShareFromRoute(session, baseurl, tenant, shareFromRoute, fetchParts):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "_getByShareFromRoute"
    return curl(url, session).headers(headers).params(tenant=tenant, shareFromRoute=shareFromRoute,
                                                      fetchParts=fetchParts).perform()


def list(session, baseurl, fetchParts, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "_list"
    return curl(url, session).method('post').headers(headers).params(fetchParts=fetchParts).body(body).perform()


def listByName(session, baseurl, tenant, tunnel, payMethod, name, fetchParts):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "_listByName"
    return curl(url, session).method('post').headers(headers).params(tenant=tenant, tunnel=tunnel, payMethod=payMethod,
                                                                     name=name, fetchParts=fetchParts).perform()


def listByShareFromRoutes(session, baseurl, tenant, fetchParts, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "_listByShareFromRoutes"
    return curl(url, session).headers(headers).params(tenant=tenant, fetchParts=fetchParts).body(body).perform()


def query(session, baseurl, fetchParts, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "_listByShareFromRoutes"
    return curl(url, session).method('post').headers(headers).params(fetchParts=fetchParts).body(body).perform()


def effect(session, baseurl, uuid, version, s):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_effect'
    return curl(url, session).headers(headers).params(**{
        'uuid': uuid,
        'versin': version,
        "string": s
    }).perform()


def saveModify(session, baseurl, s, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_saveModify'
    return curl(url, session).method('post').headers(headers).params(**{"string": s}).body(body).perform()


def saveNew(session, baseurl, query, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_saveNew'
    return curl(url, session).method('post').headers(headers).params(**{"string": query}).body(body).perform()


def setDefaultShare(session, baseurl, uuid, defaultShare, version, s):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_setDefaultShare'
    return curl(url, session).headers(headers).params(**{
        "uuid": uuid,
        "defaultShare": defaultShare,
        "version": version,
        "string": s
    }).perform()
