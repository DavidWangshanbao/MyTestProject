# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def existsAccessKey(session, baseurl, bloc, accessKey):
    """
    校验accessKey集团内唯一
    :param sessoin:
    :param baseurl:
    :param bloc:
    :param accessKey:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/authen/existsAccessKey".format(bloc=bloc)
    return curl(url, session).headers(headers).params(accessKey=accessKey).perform()