# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def checkisbeenoffsetbyticket(session, baseurl, bloc, project, featureCode, tradeSource, tradeSourceNumber):
    """
    检查是否被交易小票或日结小票压单
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param featureCode:特征码
    :param tradeSource: 交易来源
    :param tradeSourceNumber:交易来源单号
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/checkisbeenoffsetbyticket'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(featureCode=featureCode, tradeSource=tradeSource,
                                                      tradeSourceNumber=tradeSourceNumber).perform()


def downloadMemberTrade(session, baseurl, bloc, project, body):
    """
    查询会员交易明细报表下载
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/downloadMemberTrade'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def downloadTrade(session, baseurl, bloc, project, body):
    """
    查询交易明细报表下载
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/downloadTrade'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def get(session, baseurl, bloc, project, uuid):
    """
    根据uuid查询单条交易
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param uuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/get'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(uuid=uuid).perform()


def getByTradeNumber(session, baseurl, bloc, project, tradeNumber):
    """
    根据单号查询单条交易
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param tradeNumber:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/getByTradeNumber'.format(bloc=bloc, project=project)
    return curl(url, session).headers(headers).params(tradeNumber=tradeNumber).perform()


def query(session, baseurl, bloc, project, body):
    """
    查询交易单汇总
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/query'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def querymembertrade(session, baseurl, bloc, project, body):
    """
    查询会员交易明细报表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project: 项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/querymembertrade'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def upgradeBeenOffsetInfo(session, baseurl, bloc, project):
    """
    升级交易小票和日结小票被压单信息
    :param session:
    :param baseurl:
    :param bloc: 集团
    :param project: 项目
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/trade/upgradeBeenOffsetInfo'.format(bloc=bloc, project=project)
    return curl(url, session).method('post').headers(headers).perform()
