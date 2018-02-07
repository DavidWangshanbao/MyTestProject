# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/fileUpload/phoneImage"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, token):
    """

    :param session:
    :param baseurl:
    :param token:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).headers(headers).params(token=token).perform()


def url(session, baseurl, type, limit):
    """

    :param session:
    :param baseurl:
    :param type:
    :param limit:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "url"
    return curl(url, session).headers(headers).params(token=type, limit=limit).perform()
