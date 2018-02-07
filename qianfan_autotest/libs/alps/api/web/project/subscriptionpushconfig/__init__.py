# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc, project, uuid):
    """
    查询订阅推送配置
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getbynumber(session, baseurl, bloc, project, number):
    """
    通过推送编号查询订阅推送配置
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param number:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/getbynumber'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(number=number).perform()


def parsemail(session, baseurl, bloc, project, dataSourceNumbers, mailBody, isMailBody):
    """
    解析邮件
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param dataSourceNumbers:
    :param mailBody:
    :param isMailBody:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/parsemail'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers). \
        params(isMailBody=isMailBody, dataSourceNumbers=dataSourceNumbers, mailBody=mailBody).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询订阅推送配置列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param dataSourceNumbers:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, bloc, project, uuid, version):
    """
    修改订阅推送配置
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid: string
    :param version: long
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('delete').headers(headers).params(uuid=uuid, version=version).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    查询订阅推送配置列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param dataSourceNumbers:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, project, body):
    """
    新建订阅推送配置
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param dataSourceNumbers:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/subscriptionpushconfig/savenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
