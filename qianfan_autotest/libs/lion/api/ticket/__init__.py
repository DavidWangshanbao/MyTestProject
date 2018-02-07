# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/ticket"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def create(session, baseurl, title, content, machineCode, shopId, shopName, typeId=None, priority=None, body=None):
    """
    新建工单
    :param session:
    :param baseurl:
    :param title:
    :param content:
    :param machineCode:
    :param shopId:
    :param shopName:
    :param typeId:
    :param priority:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "create"
    ocurl = curl(url, session).method('post').headers(headers).params(title=title, content=content,
                                                                      machineCode=machineCode, shopId=shopId,
                                                                      shopName=shopName)
    if typeId:
        ocurl.params(typeId=typeId)
    if priority:
        ocurl.params(priority=priority)
    if body:
        ocurl.body(body)
    return ocurl.perform()


def get_feedbacks(session, baseurl, sheetId):
    """
    工单回复明细
    :param session:
    :param baseurl:
    :param sheetId: 工单id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "feedbacks/get"
    return curl(url, session).headers(headers).params(sheetId=sheetId).perform()


def list(session, baseurl, start, limit, _filter=None, _sort=None):
    """
    查询当前用户的所有工单
    :param session:
    :param baseurl:
    :param start:
    :param limit:
    :param _filter:
    :param _sort:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "list"
    ocurl = curl(url, session).headers(headers).params(start=start, limit=limit)
    if _filter:
        ocurl.params(filter=_filter)
    if _sort:
        ocurl.params(sort=_sort)
    return ocurl.perform()

def type_list(session,baseurl):
    """
    列出所有的工单分类
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "type/list"
    return curl(url,session).headers(headers).perform()
