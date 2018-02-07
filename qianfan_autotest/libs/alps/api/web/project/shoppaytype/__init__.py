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
    查询商铺付款类型
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/shoppaytype/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询商铺付款类型列表
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/shoppaytype/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def remove(session, baseurl, bloc, project, uuid, version):
    """
    删除商铺付款类型
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/shoppaytype/remove'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def savenew(session, baseurl, bloc, project, body):
    """
    新建商铺付款类型
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/shoppaytype/savenew'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savemodify(session, baseurl, bloc, project, body):
    """
    修改商铺付款类型
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/shoppaytype/savemodify'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()
