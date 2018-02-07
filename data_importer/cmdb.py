# -*- coding: UTF-8 -*-
"""
 CMDB 操作行为的封装
"""
from __future__ import unicode_literals
import datetime, time
import pymysql, json
import os
import six
from pymysql import OperationalError
from retrying import retry

from const import RDS_RETRY_NUM, RDS_TIMEOUT
from settings import get_config, get_active_profile

dnet_global_confg = get_config()
active_profile = get_active_profile()
from playhouse.shortcuts import model_to_dict
from cmdb_orm import *


def get_rds_info_by_shopid(shopid):
    """
     通过门店id 查询到对应的数据库连接信息
    :param shopid:  门店id号
    :return:
    """
    record = Cmdbshop.get(Cmdbshop.id == shopid)
    stackid = record.stackid
    dbname = record.dbname
    # 按固定规则生成rdsid
    rdsid = "rds-{}".format(stackid)
    rs = Rds.get(Rds.id == rdsid)
    return {
        "shopid": shopid,
        "host": rs.ip,
        "username": rs.username,
        "password": rs.password,
        "port": int(rs.port),
        "internalip": rs.internalip,
        "dbname": dbname
    }


def retry_OperationalError(exception):
    print("retry:" + "---------" * 10)
    return isinstance(exception, OperationalError)


class Cmdb(CmdbService):
    conn = None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def __init__(self, _filename=None):
        if (_filename):
            filename = _filename
        else:
            filename = dnet_global_confg['cmdb_cfg']
            # print(filename)

        with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
            ds = json.load(fp)[u"datasource"]
            self.conn = pymysql.connect(host=ds[u"host"], db=ds[u"db"], password=ds[u"password"], user=ds[u"user"],
                                        charset=ds[u'charset'],
                                        connect_timeout=RDS_TIMEOUT, read_timeout=RDS_TIMEOUT,
                                        write_timeout=RDS_TIMEOUT)
            # self.conn = pymysql.connect(host="rm-bp1i5vf5u8360y5t8.mysql.rds.aliyuncs.com", db="toolset_cmdb",password= "Lm7Rh7lw",user= "toolset_cmdb")
            # self.conn = pymysql.connect("rm-bp1z7q6kceyvq6j54o.mysql.rds.aliyuncs.com","cmdb","Lm7Rh7lw","cmdb")

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getDockerHub(self, env=None):
        env = env or dnet_global_confg['stack_environment']
        dockerHub = None
        try:
            for dockerHub in Dockerhub.select():
                environments = dockerHub.environment.split(",")
                if env in environments:
                    return dockerHub
            return dockerHub
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getAccessKey(self):
        raise NotImplementedError()

    # stack
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findStack(self, stackId, env=None):
        env = env or dnet_global_confg['stack_environment']
        return Stack.get(Stack.id == stackId)

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findStacksByEnvironment(self, env=None):
        env = env or dnet_global_confg['stack_environment']
        if (env != dnet_global_confg['stack_environment']):
            raise Exception("the stack envrionment(%s) does not belongs to current profile %s" % (env, active_profile))
        stacks = []
        result = Stack.select().where(Stack.environment == env)
        for r in result:
            stacks.append(r)

        return stacks

    def findHostByEnvironment(self):
        try:
            stackIds = self.findStackIdsByEnvironment()
            return Host.select().where(Host.stackid.in_(stackIds))
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getHostsByEnvironment(self):
        hosts = []
        for stack in self.findStacksByEnvironment():
            _hosts = self.getHosts(stack)
            hosts.extend(_hosts)
        return hosts

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findStackIdsByEnvironment(self, env=None):
        env = env or dnet_global_confg['stack_environment']
        if (env != dnet_global_confg['stack_environment']):
            raise Exception("the stack envrionment(%s) does not belongs to current profile %s" % (env, active_profile))
        stackIds = []
        result = Stack.select(Stack.id).where(Stack.environment == env)
        for r in result:
            stackIds.append(r.id)
        return stackIds

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findStackIdsByType(self, type, env=None):
        stackIds = []
        env = env or dnet_global_confg['stack_environment']
        if (env != dnet_global_confg['stack_environment']):
            raise Exception("the stack envrionment(%s) does not belongs to current profile %s" % (env, active_profile))
        result = Stack.select(Stack.id).where((Stack.environment == env) & (Stack.type == type))
        for r in result:
            stackIds.append(r.id)
        return stackIds

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getStackRds(self, stackId):
        try:
            return Rds.get(Rds.stackid == stackId)
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getRedises(self, stackId):
        try:
            return Redis.select().where(Redis.stackid == stackId)
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getHosts(self, stack):
        try:
            return Host.select().where(Host.stackid == stack.id)
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getHostIds(self, stack):
        try:
            return Host.select(Host.id).where(Host.stackid == stack.id)
        except DoesNotExist:
            return []

    # planjob
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getHostsforPlanJob(self, stackId):
        try:
            return Host.select().where(Host.stackid == stackId)
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findJobName(self, planJob):
        raise NotImplementedError

    # host
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findHost(self, hostId):
        try:
            return Host.get(Host.id == hostId)
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findHostIP(self, hostId):
        try:
            return Host.select(Host.publicip, Host.innerip).where(Host.id == hostId).get()
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getContainerStatuses(self, id):
        try:
            return Containerstatus.select()
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getAllContainers(self):
        try:
            return Container.select()
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getContainers(self, hostId):
        try:
            if not (isinstance(hostId, six.string_types)):
                raise ValueError("not support value type")

            return Container.select().where(Container.hostid == hostId)
        except DoesNotExist:
            return []

    # container
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findContainer(self, containerId):
        try:
            return Container.get(Container.id == containerId)
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def updateContainerForImageVersion(self, container_id, image_version):
        r = Container.get(Container.id == container_id)
        r.imageversion = image_version
        r.save()

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def deleteContainerForImageVersion(self, container_id):
        r = Container.get(Container.id == container_id)
        r.imageversion = 'deleted'
        r.save()

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getContainersByImage(self, image, imageVersion):
        try:
            return Container.select().where((Container.image == image) & (Container.imageversion == imageVersion))
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getContainersByImageAndStackid(self, image, stackid):
        return Container.select().where(Container.image == image, Container.stackid == stackid)

    # rds
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getRds(self, stackId):
        try:
            return Rds.get(Rds.stackid == stackId)
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getRdsByStackAndUser(self, stackId, username):
        return Rds.get(Rds.stackid == stackId, Rds.username == username)

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getAllRds(self, stackId):
        try:
            return Rds.select().where(Rds.stackid == stackId)
        except DoesNotExist:
            return []

    # rdsDb
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getRdsUsedDbs(self):
        try:
            return Dbused.select()
        except DoesNotExist:
            return []

    # rdsDb
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getRdsDbs(self, rds):
        try:
            return Rdsdb.select().where(Rdsdb.rdsid == rds.id)
        except DoesNotExist:
            return []

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getRdsDb(self, rds):
        return Rdsdb.get(Rdsdb.rdsid == rds.id)

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def insertRdsDb(self, rdsdb):
        raise NotImplementedError

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def insertRdsDbUsed(self, dbused):
        raise NotImplementedError

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def createJob(self, host, cronExperssion, jobName, stackId=None, state=1):
        raise NotImplementedError

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def updateJob(self, cronExperssion, jobName):
        raise NotImplementedError

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def deleteJob(self, jobName):
        raise NotImplementedError

    # jobLog
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def createJobLog(self, host, cronExperssion, jobName, action, stackId=None, state=1):
        raise NotImplementedError

    # image
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getImage(self, name, tag):
        try:
            return Image.get((Image.name == name) & (Image.tag == tag))
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def runNameTag(self, img, tag):
        try:
            result = Image.get((Image.name == img) & (Image.tag == tag))
            return result.name
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def insertImage(self, name, tag, environment):
        image = Image.create(name=name, tag=tag, environment=environment)
        image.save()

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def updateImage(self, environment, name, tag):
        image = Image.get((Image.name == name) & (Image.tag == tag))
        image.environment = environment
        image.save()

    # oss
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findOss(self, stackId, appName=None):
        try:
            if appName:
                return Oss.get((Oss.stackid == stackId) & (Oss.image == appName))
            else:
                return Oss.get((Oss.stackid == stackId))

        except DoesNotExist:
            return None

    # redis
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findRedis(self, stackId, appName=None):
        if not stackId:
            raise ValueError("stack id can't be Empty")
        try:
            if appName:
                return Redis.get((Redis.image == appName) & (Redis.stackid == stackId))
            else:
                return Redis.get(Redis.stackid == stackId)
        except DoesNotExist:
            return None

    # opensearch
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findOpenSearch(self, stackId):
        try:
            return Opensearch.get(Opensearch.stackid == stackId)
        except DoesNotExist:
            return None

    # containerstatus
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def findContainerStatus(self, id):
        try:
            return Containerstatus.get(Containerstatus.id == id)
        except DoesNotExist:
            return None

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def insertContainerStatus(self, id, status, detail):
        q = Containerstatus.insert(id=id, status=status, detail=detail)
        q.execute()

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def updateContainerStatus(self, id, status, detail):
        q = Containerstatus.update(status=status, detail=detail).where(Containerstatus.id == id)
        q.execute()

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def deleteContainerStatus(self, id):
        Containerstatus.delete().where(Containerstatus.id == id)

    # cmdbShop
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getCmdbShopId(self):
        raise NotImplementedError

    # nginx
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getNginxs(self):
        nginxs = []
        for stack in self.findStacksByEnvironment():
            _nginx = Nginx.select().where(Nginx.stackid == stack.id)
        nginxs.extend(_nginx)
        return nginxs

    # slb
    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def getSlbVgroupByServerAndport(self, serverid, port):
        return Slbvgroup.select().where(Slbvgroup.serverid == serverid, Slbvgroup.port == port)

    @retry(stop_max_attempt_number=RDS_RETRY_NUM, retry_on_exception=retry_OperationalError)
    def get_rds_info_by_dbname(self ,dbname):
        stacks = self.findStackIdsByType("plat")
        stackId = filter(lambda x : self.getRds(x) != None and dbname in map(lambda y : y.name , self.getRdsDbs(self.getRds(x)) ) ,stacks)[0]
        rds = self.getRds(stackId)
        return {
            "host": rds.ip,
            "username": rds.username,
            "password": rds.password,
            "port": int(rds.port),
            "internalip": rds.internalip,
            "dbname": dbname
        }