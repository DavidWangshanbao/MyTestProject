# coding=utf-8
from __future__ import unicode_literals, print_function
import sys
from utils import curl,baseurl_strip
reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/user'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def login(session, baseurl, user, password, token):
    """
    dbo 登录
    :param session:
    :param baseurl:
    :param user:
    :param password:
    :param token:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "login"
    params = {
        "password": password,
        "token": token,
        "user": user
    }
    # return session.get(url, params=params, timeout=5)
    return curl(url,session).params(**params).perform(timeout=5)

def logout(session,baseurl):
    """
    dbo 登出
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "logout"
    return curl(url,session).perform(timeout=5)

