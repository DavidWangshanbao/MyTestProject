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
    查询销售计划模板详情
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplantemplate/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询销售计划模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplantemplate/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, bloc, project, uuid, version):
    """
    删除计划模板
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplantemplate/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('delete').headers(headers).params(uuid=uuid, version=version).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    修改计划模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplantemplate/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, project, body):
    """
    新建销售计划模板模板
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/saleplantemplate/savenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
