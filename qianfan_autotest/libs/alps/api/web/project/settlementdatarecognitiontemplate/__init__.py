# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def disable(session, baseurl, bloc, project, uuid,version):
    """
    停用日结小票数据识别模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/disable'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid,version=version).perform()



def enable(session, baseurl, bloc, project, uuid,version):
    """
    启用日结小票数据识别模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/enable'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid,version=version).perform()

def get(session, baseurl, bloc, project, uuid):
    """
    查询日结小票数据识别模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()

def getmaxpriority(session, baseurl, bloc, project, collectionTerminalNo,ticketType,settlementType):
    """
    根据采集点编号、模板类型获取日结小票数据识别模板的最大优先级
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param collectionTerminalNo:
    :param ticketType:
    :param settlementType:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/getmaxpriority'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(ticketType=ticketType,collectionTerminalNo=collectionTerminalNo,settlementType=settlementType).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询数据识别模板列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()

def remove(session, baseurl, bloc, project, uuid,version):
    """
    删除日结小票数据识别模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid,version=version).perform()

def savemodify(session, baseurl, bloc, project, body):
    """
    修改日结小票数据识别模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()

def savenew(session, baseurl, bloc, project, body):
    """
    保存日结小票数据识别模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/settlementdatarecognitiontemplate/savenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
