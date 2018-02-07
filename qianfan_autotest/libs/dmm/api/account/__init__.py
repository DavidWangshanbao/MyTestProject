# coding=utf-8
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/accounts"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def tenants(session, baseurl, accountId):
    """
    查询配置商户列表
    :param session:
    :param baseurl:
    :param accountId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{accountId}/tenants'.format(accountId=accountId)
    return curl(url, session).headers(headers).perform()


def set_tenants(session, baseurl, accountId, body):
    """
    设置商户
    :param session:
    :param baseurl:
    :param body: (RequestBody) SetTenants
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{accountId}/tenants'.format(accountId=accountId)
    return curl(url, session).method('put').headers(headers).body(body).perform()


def get_account_by_paycanal(session, baseurl, route, channel, page, pageSize, keywords=None):
    """
    查询支付渠道下的账户列表
    :param session:
    :param baseurl:
    :param route:
    :param channel:
    :param page:
    :param pageSize:
    :param keywords: required = false
    :return:
    """
    url = _get_prefix(baseurl)
    ocurl = curl(url, session).headers(headers).params(
        route=route, channel=channel, page=page, pageSize=pageSize
    )
    if keywords:
        ocurl.params(keywords=keywords)
    return ocurl.perform()


def get_account_by_accountId(session, baseurl, accountId):
    """
    查询支付账户
    :param session:
    :param baseurl:
    :param accountId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + accountId
    return curl(url, session).headers(headers).perform()


def set_default_share(session, baseurl, accountId, defaultShare, version):
    """
    设置默认共享账户
    :param session:
    :param baseurl:
    :param accountId:
    :param defaultShare:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{accountId}/default/{defaultShare}'.format(accountId=accountId, defaultShare=defaultShare)
    return curl(url, session).method('put').headers(headers).params(version=version).perform()


def open_and_stop_account(session, baseurl, accountId, onOrOff, version):
    """
    开启/关闭账户
    :param session:
    :param baseurl:
    :param accountId:
    :param onOrOff:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{accountId}/default/{onOrOff}'.format(accountId=accountId, onOrOff=onOrOff)
    return curl(url, session).method('put').headers(headers).params(version=version).perform()


def remove_account(session, baseurl, accountId, version):
    """
    删除支付账户
    :param session:
    :param baseurl:
    :param accountId:
    :param version:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + accountId
    return curl(url, session).method('delete').headers(headers).params(version=version).perform()
