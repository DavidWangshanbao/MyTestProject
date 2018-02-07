# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/wx/oauth2/fake"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def lotteryHome(session, baseurl, activityId):
    """
    正式的活动页面，需要微信认证
    :param session:
    :param baseurl:
    :param activityId:
    :return:
    """
    url = _get_prefix(baseurl) + 'lotteryHome'
    ocurl = curl(url, session).headers(headers).params(activity=activityId)
    return ocurl.perform()
