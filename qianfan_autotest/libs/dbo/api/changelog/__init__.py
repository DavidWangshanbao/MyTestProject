# coding=utf-8
from __future__ import unicode_literals, print_function
import sys
from utils import curl, headers, baseurl_strip

reload(sys)
sys.setdefaultencoding('utf-8')

PREFIX = 's/changeLog'


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl

