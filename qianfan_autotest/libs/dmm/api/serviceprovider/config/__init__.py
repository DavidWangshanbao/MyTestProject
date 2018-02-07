# coding=utf-8
from __future__ import unicode_literals, print_function
from utils import baseurl_strip, curl, headers

PREFIX = "web/shop/shopConfig"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def save(session, baseurl, body):
    """

    :param session:
    :param baseurl:
    :param body: (RequestBody) BServiceProviderConfig like python dict object
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'save'
    return curl(url, session).headers(headers).method('post').body(body).perform(timeout=5)


def update(session, baseurl, body):
    """

    :param session:
    :param baseurl:
    :param body: (RequestBody) BServiceProviderConfig like python dict object
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'save'
    return curl(url, session).headers(headers).method('post').body(body).perform(timeout=5)


def get(session, baseurl, id):
    """

    :param session:
    :param baseurl:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).params(id=id).headers(headers).perform(timeout=5)
