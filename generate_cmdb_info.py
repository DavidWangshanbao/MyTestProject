#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
from logger import Logger, ConsoleAppender, LogStashAppender, CompositeAppender
from eliot import write_traceback, add_destination
from utils import __LINE__, readFromFile, writeLinesToFile,printStack
from cmdb import *
from jinja2 import Template
from toolz import pluck

exit_code = 0

RDSDBUSED_SLOTS = ['dbid', 'currentshopcount', "used"]
OSS_SLOTS = ['id', "stackid", 'url', 'internalurl', "bucketname", 'objectbaseurl']
RDS_SLOTS = ['id', 'stackid', "ip", "port", 'username', 'password', 'rdsinstanceid']
OPENSEARCH_SLOTS = ['stackid', 'shopsku', 'platshopsku']
RDSDB_SLOTS = ['id', 'rdsid', 'name']
STACK_SLOTS = ["id", "type", "environment", "dbcount", "shopcountperdb", "currentshopcount"]
REDIS_SLOTS = ["id", 'stackid', 'publicip', 'intranetip', 'port', 'password', 'image', 'db']
HOST_SLOTS = ['id', "name", "innerip", "stackid"]
CONTAINER_SLOTS = ['id', "image", "imageversion", "port", "portssl", "portjvm", "hostid"]
def getHostsInfo(stacks, cmdb):
    result = []
    try:
        for stack in stacks:
            result.extend(cmdb.getHosts(stack))
        for item in result:
            item.stack = item.stackid

        return result
    except Exception as e:
        printStack()
        exit_code =1


def getContainersInfo(hostids, cmdb):
    try:
        result = []
        for hostid in hostids:
            result.extend(cmdb.getContainers(hostid))
        result = map(lambda x: model_to_dict(x), result)
        result =  list(pluck(list(CONTAINER_SLOTS), result))
        result = filter(lambda  x:x[2]!=None,result)
        def helper(x):
            import  copy
            result = list(copy.copy(x))
            if (result[3]==None):
                result[3] = 'None'
            if (result[4] == None):
                result[4] = 'None'
            if (result[5] == None):
                result[5] = 'None'
            return tuple(result)
        result = map(lambda x:helper(x),result)


        return  result
    except Exception as e:
        printStack()
        exit_code = 1


def getOSSsInfo(stacks, cmdb):
    result = []

    try:
        for stack in stacks:
            result.append(cmdb.findOss(stack.id))
        for item in result:
            item.id = unicode(item.id) if isinstance(item.id,int) else item.id
        result =  list(pluck(list(OSS_SLOTS), map(lambda x: model_to_dict(x), result)))
        result= map(lambda x:list(x),result)
        return result
    except Exception as e:
        printStack()
        exit_code = 1


def getRedisesInfo(stacks, cmdb):
    result = []
    try:
        for stack in stacks:
            result.extend(cmdb.getRedises(stack.id))
        for item in result:
            item.id = unicode(item.id) if isinstance(item.id, int) else item.id
        result = list(pluck(list(REDIS_SLOTS), map(lambda x: model_to_dict(x), result)))
        result = map(lambda x: list(x), result)
        return filter(None,result)
    except Exception as e:
        printStack()
        exit_code = 1


def getOpensearchesInfo(stacks, cmdb):
    result = []
    try:
        for stack in stacks:
            result.append(cmdb.findOpenSearch(stack.id))
        result = map(lambda x: model_to_dict(x), filter(None, result))
        return result
    except Exception as e:
        printStack()
        exit_code = 1


def getRdsesInfo(stacks, cmdb):
    result = []
    rdses = []
    try:
        for stack in stacks:
            rdses.append(cmdb.getRds(stack.id))
        # result = list(pluck(list(RDS_SLOTS), rdses))
        result = map(lambda x: list(x), result)
        return (result,rdses)
    except Exception as e:
        printStack()
        exit_code = 1

def getRdsdbesInfo(rdses, cmdb):
    result = []
    rdsdbs = []
    try:
        for rds in rdses:
            rdsdbs.extend(cmdb.getRdsDbs(rds))
        for rdsdb in rdsdbs:
            rdsdb.rdsid = rdsdb.id
        # result = list(pluck(list(RDSDB_SLOTS),  rdsdbs))
        result = map(lambda x: list(x), result)
        return (result,rdsdbs)
    except Exception as e:
        printStack()
        exit_code =1

def getRdsUseddbesInfo(rdses, cmdb):
    result = []
    rdsuseddbs = []
    # try:
    rdsuseddbs.extend(cmdb.getRdsUsedDbs())
    result = list(pluck(list(RDSDBUSED_SLOTS), map(lambda x: model_to_dict(x), rdsuseddbs)))
    result = map(lambda x: list(x), result)
    result = map(lambda x:[ unicode(i) for i in x],result)
    return filter(lambda x: x[0] and x[1] and x[2],result)
    # except Exception as e:
    #     printStack()
    #     exit_code =1


if __name__ == "__main__":
    try:
        logger = Logger()
        logger.setAppender(CompositeAppender(ConsoleAppender(), LogStashAppender()))
        cmdb = Cmdb()
        cmdb_stacks = cmdb.findStacksByEnvironment(dnet_global_confg['stack_environment'])

        t = Template(readFromFile("templates/cmdbInfo.tpl"))
        hostinfos = getHostsInfo(cmdb_stacks, cmdb)
        rdsinfos ,rdses = getRdsesInfo(cmdb_stacks,cmdb)
        rdsdbinfos,rdsdbs = getRdsdbesInfo(rdses,cmdb)

        res = t.render(stack_headers="|".join(STACK_SLOTS),
                       stack_table_line_sep="|".join(['---'] * len(STACK_SLOTS)),
                       stackinfo=list(pluck(list(STACK_SLOTS), map(lambda x: model_to_dict(x), cmdb_stacks))),
                       host_headers="|".join(HOST_SLOTS),
                       host_table_line_sep="|".join(['---'] * len(HOST_SLOTS)),
                       hostinfo=list(pluck(list(HOST_SLOTS), map(lambda x:model_to_dict(x),hostinfos)))
                       , container_headers="|".join(CONTAINER_SLOTS),
                       container_table_line_sep="|".join(['---'] * len(CONTAINER_SLOTS)),
                       containerinfo=getContainersInfo(map(lambda x:x.id,hostinfos), cmdb)
                       , oss_headers="|".join(OSS_SLOTS),
                       oss_table_line_sep="|".join(['---'] * len(OSS_SLOTS)),
                       ossinfo=getOSSsInfo(cmdb_stacks, cmdb)
                       , redis_headers="|".join(REDIS_SLOTS),
                       redis_table_line_sep="|".join(['---'] * len(REDIS_SLOTS)),
                       redisinfo=getRedisesInfo(cmdb_stacks, cmdb)
                       , opensearch_headers="|".join(OPENSEARCH_SLOTS),
                       opensearch_table_line_sep="|".join(['---'] * len(OPENSEARCH_SLOTS)),
                       opensearchinfo=getOpensearchesInfo(cmdb_stacks, cmdb)
                       , rds_headers="|".join(RDS_SLOTS),
                       rds_table_line_sep="|".join(['---'] * len(RDS_SLOTS)),
                       rdsinfo=rdsinfos
                       , rdsdb_headers="|".join(RDSDB_SLOTS),
                       rdsdb_table_line_sep="|".join(['---'] * len(RDSDB_SLOTS)),
                       rdsdbinfo=rdsdbinfos
                       , dbused_headers="|".join(RDSDBUSED_SLOTS),
                       dbused_table_line_sep="|".join(['---'] * len(RDSDBUSED_SLOTS)),
                       dbusedinfo= getRdsUseddbesInfo(rdses,cmdb)
                       )

        if os.path.exists('cmdbInfo.html'):
            os.remove('cmdbInfo.html')
        if os.path.exists('cmdbInfo.md'):
            os.remove('cmdbInfo.md')

        writeLinesToFile('cmdbInfo.md', [res])
        from markdowntohtml.MarkdownPreview import MarkdownCompiler, save_utf8

        compiler = MarkdownCompiler()
        html, body = compiler.run(None, True, preview=False, contents=readFromFile("cmdbInfo.md"))

        save_utf8("cmdbInfo.html", html)
        contents = readFromFile("cmdbInfo.html")



    except Exception as e:
        import cStringIO

        _file = cStringIO.StringIO()
        printStack(_file)
        print(_file.getvalue())
        logger.error(filename=__file__, lineno=__LINE__(), message=_file.getvalue(), action="generate_cmdb_info", error_code=1)
        # write_traceback()
        exit_code = 1
    finally:
        exit(exit_code)
