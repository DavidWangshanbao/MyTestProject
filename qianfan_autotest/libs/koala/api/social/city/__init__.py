# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/social/city"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, uuid):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_get'
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getById(session, baseurl, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_getById'
    return curl(url, session).headers(headers).params(id=id).perform()


def query(session, baseurl, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '_query'
    return curl(url, session).headers(headers).body(body).perform()
