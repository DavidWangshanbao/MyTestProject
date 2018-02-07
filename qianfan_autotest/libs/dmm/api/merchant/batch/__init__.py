# coding=utf-8
import json
from utils import baseurl_strip, headers, curl

PREFIX = "web/web/merchant/batch"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def add(session, baseurl, payment, afile):
    """
    批量开户
    excel不大于5M, 只支持xls和xlsx格式, 只有一列，为手机号码
    :param session:
    :param baseurl:
    :param payment: 通道
    :param afile: (RequestBody) MultipartFile
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "add"
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').params(payment=payment).perform(files=files)


def modifyRate(session, baseurl, body, channelRate):
    """
    批量修改费率
    :param session:
    :param baseurl:
    :param body: (RequestBody) List<String>
    :param channelRate:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "modifyRate"
    return curl(url, session).method('post').headers(headers).body(body).params(channelRate=channelRate).perform()
