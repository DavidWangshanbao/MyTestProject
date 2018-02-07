# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "s/app/v2/fileUpload"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def uploadImage(session, baseurl, type, files):
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + "uploadImage/{type}".format(type=tuple)
    return curl(url, session).method('post').headers(headers).params(files=files).perform()
