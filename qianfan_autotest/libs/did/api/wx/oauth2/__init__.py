# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/wx/oauth2"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def createJsapiSignature(session, baseurl, url):
    """
    创建js接口调用票据
    :param session:
    :param baseurl:
    :param url: 需要签名的url
    :return:
    """
    url = _get_prefix(baseurl) + 'createJsapiSignature'
    return curl(url, session).headers(headers).params(url=url).perform()


def forwardToWx(session, baseurl, activity, state=None):
    """
    转发请求到微信
    :param session:
    :param baseurl:
    :param activity:
    :param state:转发人的openId，可以不填
    :return:
    """
    url = _get_prefix(baseurl) + 'forwardToWx'
    ocurl = curl(url, session).headers(headers).params(activity=activity)
    if state:
        ocurl.params(state=state)
    return ocurl.perform()


def lotteryHome(session, baseurl, activity, code, state=None):
    """
    正式的活动页面，需要微信认证
    :param session:
    :param baseurl:
    :param activity:
    :param code:
    :param state:
    :return:
    """
    url = _get_prefix(baseurl) + 'lotteryHome'
    ocurl = curl(url, session).headers(headers).params(activity=activity, code=code)
    if state:
        ocurl.params(state=state)
    return ocurl.perform()
