# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = 'web/web/menus'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def get(session, baseurl, serviceProviderUuid):
    """
    查询服务商菜单
    :param session:
    :param baseurl:
    :param serviceProviderUuid:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'get'
    return curl(url, session).headers(headers).params(serviceProviderUuid=serviceProviderUuid).perform()
