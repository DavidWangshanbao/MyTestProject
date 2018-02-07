# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/dpos/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def check_mobile(session, baseurl, tenant, mobile):
    """
    根据手机号验证是否已经存在该商户的会员,返回true表示存在
    :param session:
    :param baseurl:
    :param tenant:
    :param mobile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/check/mobile".format(tenant=tenant)
    return curl(url, session).headers(headers).params(mobile=mobile).perform()


def detail(session, baseurl, tenant, id):
    """
    会员详情
    :param session:
    :param baseurl:
    :param tenant:
    :param id:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/detail".format(tenant=tenant)
    return curl(url, session).headers(headers).params(id=id).perform()


def query(session, baseurl, tenant, body):
    """
    会员分页查询
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/query".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def query_conditions(session, baseurl, tenant):
    """
    会员查询条件
    :param session:
    :param baseurl:
    :param tenant:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/query/conditions".format(tenant=tenant)
    return curl(url, session).headers(headers).perform()


def modify(session, baseurl, tenant, body):
    """
    编辑会员
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/save/modify".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def new(session, baseurl, tenant, body):
    """
    新增会员
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/save/new".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def set_tags(session, baseurl, tenant, member, version, body):
    """
    设置会员标签
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :param version:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/set/tags".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers). \
        params(member=member, version=version).body(body).perform()


def set_batch_tags(session, baseurl, tenant, body):
    """
    批量设置会员标签
    :param session:
    :param baseurl:
    :param tenant:
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/set/tags/batch".format(tenant=tenant)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def statices(session, baseurl, tenant, member):
    """
    会员消费充值统计,如果出现会员从来没有消费过的请况，最近消费时间=null，间隔天数=-1
    :param session:
    :param baseurl:
    :param tenant:
    :param member:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/statices".format(tenant=tenant)
    return curl(url, session).headers(headers).params(member=member).perform()


def import_(session, baseurl, tenant, shop, afile):
    """
    上传文件, 文件后缀必须为.xls或.xlsx, 返回本次导入唯一标识
    :param session:
    :param baseurl:
    :param tenant:
    :param shop:
    :param afile:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/import".format(tenant=tenant)
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').params(shop=shop).perform(files=files)


def import_progressbar(session, baseurl, tenant, importId):
    """
    查询导入进度，返回当前导入百分比（整数）
    :param session:
    :param baseurl:
    :param importId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/import/progressbar".format(tenant=tenant)
    return curl(url, session).headers(headers).params(importId=importId).perform()


def import_result(session, baseurl, tenant, importId):
    """
    查询导入结果
    :param session:
    :param baseurl:
    :param importId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/import/result".format(tenant=tenant)
    return curl(url, session).headers(headers).params(importId=importId).perform()


def interrupt_import(session, baseurl, tenant, importId):
    """
    终止导入
    :param session:
    :param baseurl:
    :param tenant:
    :param importId:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "{tenant}/member/import/interrupt".format(tenant=tenant)
    return curl(url, session).headers(headers).params(importId=importId).perform()
