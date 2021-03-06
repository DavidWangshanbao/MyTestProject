# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/region"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, level=None, parentCode=None):
    """

    :param session:
    :param baseurl:
    :param level:
    :param parentCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    ocurl = curl(url, session).headers(headers)
    if level:
        ocurl.params(level=level)
    if parentCode:
        ocurl.params(parentCode=parentCode)

    return ocurl.perform()
