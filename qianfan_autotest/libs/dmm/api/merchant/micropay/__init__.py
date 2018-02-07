# coding=utf-8
import json
from utils import baseurl_strip, headers, curl

PREFIX = "web/web/merchant/micropay"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def query(session, baseurl, channel):
    """
    渠道类型
    :param session:
    :param baseurl:
    :param channel:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "query"
    return curl(url, session).headers(headers).params(channel=channel).perform()
