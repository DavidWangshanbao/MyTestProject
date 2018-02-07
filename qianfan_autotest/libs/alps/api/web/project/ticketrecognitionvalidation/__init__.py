# coding=utf-8
from __future__ import unicode_literals, print_function

from utils import baseurl_strip, curl, headers

PREFIX = "pod-web/s/web"


def _get_prefix(baseurl):
    baseurl = baseurl_strip(baseurl)
    baseurl = baseurl + "/" + PREFIX + "/"
    return baseurl


def getrecognitionresult(session, baseurl, bloc, project, ticketUuid, reimagerecognition, redatarecognition):
    """
    小票识别验证
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param ticketUuid: String
    :param reimagerecognition: bool
    :param redatarecognition: bool
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketrecognitionvalidation/getrecognitionresult'.format(bloc=bloc,
                                                                                                project=project)
    return curl(url, session).headers(headers). \
        params(ticketUuid=ticketUuid, reimagerecognition=reimagerecognition,
               redatarecognition=redatarecognition).perform()


def querytickets(session, baseurl, bloc, project, body):
    """
    查询小票列表
    :param session:
    :param baseurl:
    :param bloc:集团
    :param project:项目
    :param body:
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketrecognitionvalidation/querytickets'.format(bloc=bloc,
                                                                                        project=project)
    return curl(url, session).method('post').headers(headers).body(body).perform()


def rerecognitionticket(session, baseurl, bloc, project, ticketUuid, recognitionType, version):
    """
    重新识别
    :param session:
    :param baseurl:
    :param bloc:
    :param project:
    :param ticketUuid: String
    :param recognitionType: integer
    :param version: long
    :return:
    """
    _baseurl = _get_prefix(baseurl)
    url = _baseurl + '{bloc}/{project}/ticketrecognitionvalidation/rerecognitionticket'.format(bloc=bloc,
                                                                                               project=project)
    return curl(url, session).method('post').headers(headers).params(ticketUuid=ticketUuid,
                                                                     recognitionType=recognitionType,
                                                                     version=version).perform()
