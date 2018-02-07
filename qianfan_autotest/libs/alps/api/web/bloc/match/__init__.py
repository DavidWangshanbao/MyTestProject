# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def jasonpathmatch(session, baseurl, bloc, jsonPath, body):
    """
    jasonPath匹配
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param jsonPath:
    :param body: 待匹配的文本
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/match/jasonpathmatch'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(jsonPath=jsonPath).body(body).perform()


def regexmatch(session, baseurl, bloc, regex, body):
    """
    jasonPath匹配
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param regex: 正则表达式
    :param body: 待匹配的文本
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/match/jasonpathmatch'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(regex=regex).body(body).perform()
