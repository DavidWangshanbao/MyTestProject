# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "/s/h5"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getFileByOssId(session,baseurl,tenant,storageId):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl+"{tenant}/media/getFileByOssId".format(tenant=tenant)
    return curl(url,session).headers(headers).params(storageId=storageId).perform()
