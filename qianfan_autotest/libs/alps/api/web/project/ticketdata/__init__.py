# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def batchremove(session, baseurl, bloc, project, jobInstnaceId, body):
    """
    批量删除交易小票
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param jobInstnaceId:job编号
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/batchremove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(jobInstnaceId=jobInstnaceId).body(body).perform()


def batchreprocess(session, baseurl, bloc, project, jobInstnaceId, body):
    """
    批量重新加工交易小票
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param jobInstnaceId:job编号
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/batchreprocess'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(jobInstnaceId=jobInstnaceId).body(body).perform()


def batchrerecognitionticket(session, baseurl, bloc, project, jobInstnaceId, recognitionType, body):
    """
    批量重新加工交易小票
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param jobInstnaceId:job编号
    :param recognitionType:重新识别类型
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/batchrerecognitionticket'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(jobInstnaceId=jobInstnaceId,
                                                                     recognitionType=recognitionType).body(
        body).perform()


def getbyfeaturecode(session, baseurl, bloc, project, featureCode):
    """
    根据特征码查询单条小票数据
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param poroject:项目
    :param featureCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/getbyfeaturecode'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(featureCode=featureCode).perform()


def removebyfeaturecode(session, baseurl, bloc, project, featureCode):
    """
    根据特征码删除小票数据
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param poroject:项目
    :param featureCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/removebyfeaturecode'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(featureCode=featureCode).perform()


def remove(session, baseurl, bloc, project, uuid, version):
    """
    删除小票数据
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询交易小票列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def reprocess(session, baseurl, bloc, project, featureCode):
    """
    交易小票重新加工
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param poroject:项目
    :param featureCode:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/reprocess'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(featureCode=featureCode).perform()


def save(session, baseurl, bloc, project, body):
    """
    修改小票数据
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param poroject:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketdata/reprocess'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
