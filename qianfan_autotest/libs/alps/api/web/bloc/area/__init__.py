# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getareabycondition(session, baseurl, bloc, keyword):
    """
    根据条件查询区域列表
    :param sessoin:
    :param baseurl:
    :param bloc:
    :param keyword:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/getareabycondition".format(bloc=bloc)
    return curl(url, session).headers(headers).params(keyword=keyword).perform()


def getareaorginfobyareauuid(session, baseurl, bloc, areaUuid):
    """
    查询区域包含组织
    :param session:
    :param baseurl:
    :param bloc:集团
    :param areaUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/getareaorginfobyareauuid".format(bloc=bloc)
    return curl(url, session).headers(headers).params(areaUuid=areaUuid).perform()


def gets(session, baseurl, bloc):
    """
    查询区域列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/gets".format(bloc=bloc)
    return curl(url, session).headers(headers).perform()


def query(session, baseurl, bloc, body):
    """
    查询区域列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/query".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def queryprojectbyareauuid(session, baseurl, bloc, regionUuid):
    """
    查询区域包含项目
    :param session:
    :param baseurl:
    :param bloc:集团
    :param regionUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/queryprojectbyareauuid".format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(regionUuid=regionUuid).perform()


def removeall(session,baseurl,bloc,uuid,version):
    """
    删除区域
    :param session:
    :param baseurl:
    :param bloc:集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/removeall".format(bloc=bloc)
    return curl(url,session).method('delete').headers(headers).params(uuid=uuid,version=version).perform()


def removeareorg(session, baseurl, bloc, areaUuid, organizationUuid):
    """
    删除区域包含组织
    :param session:
    :param baseurl:
    :param bloc:集团
    :param areaUuid:
    :param organizationUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/removeareorg".format(bloc=bloc)
    return curl(url,session).method('delete').headers(headers).params(uuid=areaUuid, version=organizationUuid).perform()

def savemodify(session, baseurl, bloc, body):
    """
    修改区域
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/savemodify".format(bloc=bloc)
    return curl(url,session).method('put').headers(headers).body(body).perform()

def savenewarea(session, baseurl, bloc, body):
    """
    创建区域
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/savenewarea".format(bloc=bloc)
    return curl(url,session).method('post').headers(headers).body(body).perform()

def savenewareaorg(session, baseurl, bloc, body):
    """
    添加区域包含组织
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/area/savenewareaorg".format(bloc=bloc)
    return curl(url,session).method('post').headers(headers).body(body).perform()