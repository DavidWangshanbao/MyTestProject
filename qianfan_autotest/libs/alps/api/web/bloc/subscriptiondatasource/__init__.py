# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, bloc, uuid):
    """
    查询订阅数据源
    :param session:
    :param baseurl:
    :param bloc:集团
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/get'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getbynumber(session, baseurl, bloc, number):
    """
    根据编号查询订阅数据源
    :param session:
    :param baseurl:
    :param bloc:集团
    :param number:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/getbynumber'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(number=number).perform()


def query(session, baseurl, bloc, body):
    """
    查询订阅数据源列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/query'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def querysqlrslwithvalidate(session, baseurl, bloc, sqlText):
    """
    验证数据源参数得到预览结果
    :param session:
    :param baseurl:
    :param bloc:集团
    :param sqlText:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/querysqlrslwithvalidate'.format(bloc=bloc)
    return curl(url, session).headers(headers).params(sqlText=sqlText).perform()


def remove(session, baseurl, bloc, uuid, version):
    """
    删除订阅数据源
    :param session:
    :param baseurl:
    :param bloc:集团
    :param uuid:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/remove'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).params(uuid=uuid, version=version).perform()


def savemodify(session, baseurl, bloc, body):
    """
    修改订阅数据源
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/savemodify'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def savenew(session, baseurl, bloc, body):
    """
    新建订阅数据源
    :param session:
    :param baseurl:
    :param bloc:集团
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/subscriptiondatasource/savenew'.format(bloc=bloc)
    return curl(url, session).method('post').headers(headers).body(body).perform()
