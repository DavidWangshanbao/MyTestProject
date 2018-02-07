# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/web/merchant"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def add(session, baseurl, account):
    """
    开户
    :param session:
    :param baseurl:
    :param account:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'add'
    return curl(url, session).method('post').headers(headers).body(account).perform()


def bank(session, baseurl, query):
    """
    查询银行(固定按银行代码正序排序)
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/bank"
    return curl(url, session).method('post').headers(headers).body(query).perform()


def branch(session, baseurl, query):
    """
    查询支行(固定按银行代码正序排序)
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/branch"
    return curl(url, session).method('post').headers(headers).body(query).perform()


def industry(session, baseurl, query):
    """
    获取行业信息 role:可空，为空时：查询所有实体类型，不为空时查询条件实体类型下的所有经营分类 category:可空（和role关联操作，role为空category一定为空，role不为空category可空），role不为空category为空时：查询当前role下的所有经营分类，不为空时查询当前role下的category下的所有经营范围
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "baseChannel/industry"
    return curl(url, session).method('post').headers(headers).body(query).perform()


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
    url = _baseurl + 'baseChannel/region'
    ocurl = curl(url, session).headers(headers)

    if province:
        ocurl.params(province=province)
    if city:
        ocurl.params(city=city)

    return ocurl.perform()


def batch_add(session, baseurl, payment, afile):
    """
    批量开户
    :param session:
    :param baserurl:
    :param payment:
    :param afile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "batch/add"
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').params(payment=payment).perform(files=files)


def batch_modify_rate(session, baseurl, channelRate, uuids):
    """
    批量修改费率
    :param session:
    :param baseurl:
    :param channelRate:
    :param uuids: (RequestBody)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "batch/modifyRate"
    return curl(url, session).method('post').headers(headers).params(channelRate=channelRate).body(uuids).perform()


def change_check_state(session, baseurl, userPayChannel):
    """
    审核结果配置
    :param session:
    :param baseurl:
    :param userPayChannel:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "changeChekState"
    return curl(url, session).method('post').headers(headers).params(userPayChannel=userPayChannel).perform()


def check(session, baseurl, mobile):
    """
    检查是否开户或在开户中,success=false:开户或在开户中, success=true:可开户
    :param session:
    :param baseurl:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'check'
    return curl(url, session).method('post').headers(headers).params(mobile=mobile).perform()


def dtl(session, baseurl, id):
    """
    获取用户的基础开户资料
    :param session:
    :param baseurl:
    :param id:商户id
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'dtl'
    return curl(url, session).headers(headers).params(id=id).perform()


def export(session, baseurl, query):
    """
    商户搜索导出Excel
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'export'
    return curl(url, session).method('post').body(query).perform()


def getAuditRecord(session, baseurl, userPayChannel):
    """
    获取审核记录
    :param session:
    :param baseurl:
    :param userPayChannel:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'getAuditRecord'
    return curl(url, session).headers(headers).params(userPayChannel=userPayChannel).perform()


def list(session, baseurl, query):
    """
    商户搜索
    :param session:
    :param baseurl:
    :param query:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'list'
    return curl(url, session).headers(headers).body(query).perform()


def micropay_query(session, baseurl, channel):
    """
    渠道类型
    :param session:
    :param baseurl:
    :param channel:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'micropay/query'
    return curl(url, session).headers(headers).params(channel=channel).perform()


def mod(session, baseurl, account):
    """
    编辑
    :param session:
    :param baseurl:
    :param account:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + 'mod'
    return curl(url, session).method('post').headers(headers).body(account).perform()
