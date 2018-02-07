# coding=utf-8
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 'health'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check(session, baseurl):
    """
    健康检查
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "check"
    return curl(url, session).headers(headers).perform()
