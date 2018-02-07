# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/v2/employment"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(id=id).perform()


def invite_accept(session, baseurl, shopId, inviteCode, mobile):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'invite/accept'
    return curl(url, session).headers(headers).params(shopId=shopId, inviteCode=inviteCode, mobile=mobile).perform()


def invite_generate(session, baseurl, shopId):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'invite/generate'
    return curl(url, session).headers(headers).params(shopId=shopId).perform()


def invite_join(session, baseurl, id):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'invite/join'
    return curl(url, session).headers(headers).params(id=id).perform()


def query(session, baseurl, shopId, body):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'query'
    return curl(url, session).method('post').headers(headers).params(shopId=shopId).body(body).perform()
