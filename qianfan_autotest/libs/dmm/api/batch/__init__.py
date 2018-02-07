# coding=utf-8
from utils import baseurl_strip, curl, headers

PREFIX = "web/web/batch"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def export_account_shares(session, baseurl):
    """
    导出账户与租户关系
    :param session:
    :param baseurl:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "tenants/export"
    return curl(url, session).headers(headers).perform()


def import_account_shares(session, baseurl, afile):
    """
    导入账户与租户关系
    上传文件必填, 文件后缀必须为.xls或.xlsx,resultDetailExcelUrl为设置失败的记录结果，如果全部倒入成功，该值为空
    :param session:
    :param baseurl:
    :param afile: (MultipartFile)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "tenants"
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').perform(files=files)


def import_accounts(session, baseurl, afile):
    """
    导入账户
    上传文件, 文件后缀必须为.xls或.xlsx,resultDetailExcelUrl为设置失败的记录结果，如果全部倒入成功，该值为空
    :param session:
    :param baseurl:
    :param afile: (MultipartFile)
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "accounts"
    files = {'file': open(afile, 'rb')}
    return curl(url, session).method('post').perform(files=files)
