# coding=utf-8
import json
from utils import baseurl_strip, headers, curl

PREFIX = "web/web/merchant/baseChannel"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def region(session, baseurl, province=None, city=None):
    """
    查询地址，查省时，所有参数为空
    :param session:
    :param baseurl:
    :param province:
    :param city:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "region"
    curl_obj = curl(url, session).headers(headers)

    if province:
        curl_obj.params(province=province)
    if city:
        curl_obj.params(city=city)

    return curl_obj.perform()


def industry(session, baseurl, body):
    """
    获取行业信息 \n " + "role:可空，为空时：查询所有实体类型，不为空时查询条件实体类型下的所有经营分类 \n"
      + "category:可空（和role关联操作，role为空category一定为空，role不为空category可空），"
      + "role不为空category为空时：查询当前role下的所有经营分类，不为空时查询当前role下的category下的所有经营范围
    :param session:
    :param baseurl:
    :param body: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "industry"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def bank(session, baseurl, body):
    """
    查询银行(固定按银行代码正序排序)
    :param session:
    :param baseurl:
    :param body: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "bank"
    return curl(url, session).method('post').headers(headers).body(body).perform()


def branch(session, baseurl, body):
    """
    查询支行(固定按银行代码正序排序)
    :param session:
    :param baseurl:
    :param body: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "branch"
    return curl(url, session).method('post').headers(headers).body(body).perform()
