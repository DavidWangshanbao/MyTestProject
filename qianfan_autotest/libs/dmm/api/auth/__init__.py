# coding=utf-8
from __future__ import unicode_literals, print_function

import json

from libs.dmm.api.models import BLogin
from utils import baseurl_strip, curl, headers

PREFIX = 'web/web/auth'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def login(session, baseurl, blogin):
    """
    DMM 登入
    :param session: requests session
    :param baseurl:
    :param blogin:  instance of BLogin
    :return:
    """
    if not isinstance(blogin, BLogin):
        raise ValueError("blogin is not instance of BLogin")

    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'login'
    print(url)
    j = blogin.to_json()
    return curl(url, session).method('post').headers(headers).body(j).perform()
    # return session.post(url,headers=headers, timeout=5, data=json.dumps(j, ensure_ascii=False).encode('utf-8'))


def logout(session, baseurl):
    """
    DMM 登出
    :param session: requests session
    :param baseurl:
    :return:
    """
    baseurl = _get_prefix(baseurl)
    url = baseurl + 'logout'
    return curl(url, session).perform()
    # return session.get(url,timeout=5)


def reset_password(session, baseurl, accountNo, password, authCode):
    """
    DMM 重置密码
    :param session: requests session
    :param baseurl:
    :param accountNo: 账号
    :param password:  密码
    :param authCode:  验证码
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    payload = {
        "accountNo": accountNo,
        "password": password,
        "authCode": authCode
    }
    url = _baseurl + 'password/reset'
    return curl(url, session).method('post').params(**payload).perform()
