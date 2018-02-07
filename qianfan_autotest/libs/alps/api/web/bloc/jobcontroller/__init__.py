# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getjobprogress(session, baseurl, bloc, jobInstnaceId):
    """
    获取工作进度
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param jobInstnaceId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/jobController/getjobprogress'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(jobInstnaceId=jobInstnaceId).perform()


def interruptjob(session, baseurl, bloc, jobInstnaceId):
    """
    中断工作
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param jobInstnaceId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/jobController/interruptjob'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(jobInstnaceId=jobInstnaceId).perform()
