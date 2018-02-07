# coding=utf-8
"""
广告配置
"""
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/serviceproviderSource'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session,baseurl,query):
    """
    服务商详情
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "get"
    return curl(url,session).headers(headers).body(query).perform()
