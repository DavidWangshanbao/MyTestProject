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
    批量删除小票
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param jobInstnaceId:job编号
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/batchremove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(jobInstnaceId=jobInstnaceId).body(body).perform()


def batchrerecognitionticket(session, baseurl, bloc, project, jobInstnaceId, recognitionType, body):
    """
    批量重新识别
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param jobInstnaceId:job编号
    :param recognitionType:重新识别类型
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/batchrerecognitionticket'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(jobInstnaceId=jobInstnaceId,
                                                                     recognitionType=recognitionType).body(
        body).perform()


def download(session, baseurl, bloc, project, uuids):
    """
    小票文件下载
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param uuids:Array[string]
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/download'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuids=uuids).perform()


def get(session, baseurl, bloc, project, uuid):
    """
    查询小票
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getticketcontent(session, baseurl, bloc, project, uuid):
    """
    查询小票内容
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/getticketcontent'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getticketfile(session, baseurl, bloc, project, uuid):
    """
    查询小票文件
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/getticketfile'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询小票列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, bloc, project, uuid):
    """
    删除小票
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid).perform()


def upgradeBeenOffsetInfo(session, baseurl, bloc, project):
    """
    升级交易小票和日结小票被压单信息
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticket/upgradeBeenOffsetInfo'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).perform()
