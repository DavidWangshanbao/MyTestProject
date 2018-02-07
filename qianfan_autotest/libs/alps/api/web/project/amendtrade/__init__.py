# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl

def abort(session,baseurl,bloc,project,uuid,version):
    """
    作废
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/abort".format(bloc=bloc, project=project)
    return curl(url,session).method('put').headers(headers).params(uuid=uuid,version=version).perform()


def audit(session,baseurl,bloc,project,uuid,version):
    """
    复核交易补录
    :param sesson:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/audit".format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).params(uuid=uuid, version=version).perform()


def check_isbeen_offset_by_ticket(session,baseurl,bloc,project,tradeNumber):
    """
    检查是否被交易小票或日结小票压单
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param tradeNumber: 交易流水号
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/checkisbeenoffsetbyticket".format(bloc=bloc, project=project)
    return curl(url,session).headers(headers).params(tradeNumber=tradeNumber).perform()


def delete(session,baseurl,bloc,project,uuid,version):
    """
    删除交易补录单
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/delete".format(bloc=bloc, project=project)
    return curl(url,session).method('delete').headers(headers).params(uuid=uuid,version=version).perform()


def get(session,baseurl,bloc,project,uuid):
    """
    查询交易补录单详情
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/get".format(bloc=bloc, project=project)
    return curl(url,session).headers(headers).params(uuid=uuid).perform()


def query(session,baseurl,bloc,project,body):
    """
    查询交易补录单
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/query".format(bloc=bloc, project=project)
    return curl(url,session).method('post').headers(headers).body(body).perform()

def save_audit(session,baseurl,bloc,project,body):
    """
    新建并审核交易补录
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/saveaudit".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def save_modify(session,baseurl,bloc,project,body):
    """
    修改交易补录
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/savemodify".format(bloc=bloc, project=project)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def save_new(session,baseurl,bloc,project,body):
    """
    新建交易补录
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{bloc}/{project}/amendtrade/savenew".format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()

