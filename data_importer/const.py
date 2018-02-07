# -*- coding: UTF-8 -*-

LINEBREAKER = '\\'
SSH_USER = 'dnet'
SSH_PORT = "60501"
SCRIPTHOME = '/hdapp/scripts/'
SCRIPTHOME_APPINSTALL = SCRIPTHOME + '{appVersion}/appInstall/{appName}/{host.ip}_{host.id}_{timestamp}/'
SCRIPTHOME_CREATEDB = SCRIPTHOME + 'createDb/{host.ip}_{host.id}_{timestamp}/'
SCRIPTHOME_CREATEJOB = SCRIPTHOME + 'createJob/{host.ip}_{host.id}_{timestamp}/'
SCRIPTHOME_SQLRUN = SCRIPTHOME + 'sqlrun/{host.id}/{timestamp}/'
SCRIPTHOME_DBINIT = SCRIPTHOME + 'dbinit/{host.id}/{timestamp}/'
SCRIPTHOME_SQLRUN_LOG = SCRIPTHOME + 'sqlrunlog/{host.id}/sqlrun_log.{timestamp}.txt'
SCRIPTHOME_DBINIT_LOG = SCRIPTHOME + 'dbinit/{host.id}/dbinit_log.{timestamp}.txt'
SCRIPTHOME_PLANJOB = SCRIPTHOME + "planjob/"
SCRIPTHOME_LOCALPLANJOB = 'planJob/'
SCRIPTHOME_RBCOMPONENTVERSIONSQLLOG = SCRIPTHOME + 'rbcomponentversion/'

SCRIPT_FILE_RUNSH = 'run.sh'
SCRIPT_FILE_RUNSQL = 'run_sql.py'
# =================== begin of db upgrade ============================
SCRIPT_FILE_DBINIT = 'run_dbinit.py'
SCRIPT_FILE_UTILS = 'utils.py'
SCRIPT_FILE_LOGGER = "logger.py"
SCRIPT_FILE_CONST = "const.py"
SCRIPT_FILE_SETTINGSPY = "settings.py"
SCRIPT_FILE_SETTINGSYAML = "settings.yaml"
SCRIPT_FILE_SETTINGSSCMYAML = "settings-scm.yaml"
SCRIPT_FILE_SETTINGSDLYYAML = "settings-dly.yaml"
# =================== end of db upgrade ============================
SCRIPT_DBINIT_CSV_PULL = 'pullImage.csv'
SCRIPT_DBINIT_CSV_DOCKER = 'dockerRun.csv'
SCRIPT_DBINIT_LOG = 'dbinit.log'
SCRIPT_ZIP_DOCKER_LOG = 'dockerlog.zip'
SCRIPT_FILE_CRONTAB = 'crontabfile'

DPOS_AUTH_WEB = "dpos-auth-web"
DPOS_AUTH_RS = "dpos-auth-rs"
DBO_WEB = "dbo-web"
CMDB_WEB = "cmdb-web"
DPOS_WEB = "dpos-web"
FILEBEAT = "filebeat"

## Encoding
ENCODING_FORMAT = "utf-8"

## ====================================
##  LogStash
# LOGSTASH_URL = 'http://logstash.1000sails.com:8800/'
# LOGSTASH_USER = 'logstash'
# LOGSTASH_PASSWORD = 'aoDJ0JVgkfNPjarn'
## ====================================

## ====================================
## JIRA
## ====================================
JIRA_URL= 'http://jira6.app.hd123.cn/jira'
JIRA_USER= "app-publisher"
JIRA_PASSWORD= "headingapp123"

## ====================================
##  Jenkins -- DNET_DPLOY
## ====================================
JENKINS_URL="http://172.17.11.3:8080"
JENKINS_REMOTE_URL="http://jenkins.1000sails.com:8888"
JENKINS_DNET_DEPLOY_URL=JENKINS_URL+"/job/DNET_Deploy_production"
JENKINS_ACCOUNT='buhaiqing'
JENKINS_PASSWORD='buhaiqing'

## ====================================
##  HTTP请求超时
## ====================================
HTTP_REQUEST_TIMEOUT = 8

## ====================================
##  CMDB
## ====================================

RDS_RETRY_NUM = 3
RDS_TIMEOUT = 180

## ====================================
##  datatime format
## ====================================
YYYYmmddHHMMSSf="%Y-%m-%d %H:%M:%S.%f"
YYYYmmddHHMMSS="%Y-%m-%d %H:%M:%S"
YYYYmmdd="%Y-%m-%d"


from io import open
import os
import time
import demjson
import codecs


def ts():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def json_encode(obj):
    return demjson.encode(obj, compactly=False) \
        .replace('\\n', '\n') \
        .replace('\\t', '\t') \
        .replace('\\\\', '\\')


def print_file(fileName):
    print(''.ljust(40, '-'))
    print('File: ' + fileName)
    print(''.ljust(40, '-'))
    file = open(fileName, "r", encoding="utf-8")
    print(file.read())
    file.close()


def copy_file(source, target):
    file = open(source, "r", encoding="utf-8")
    lines = file.read()
    file.close()

    path = target[0:target.rindex('/')]
    if not os.path.exists(path): os.makedirs(path)
    file = open(target, "w", encoding="utf-8", newline='\n')
    file.write(lines)
    file.close()


def copy_file_repl(source, target, repl):
    file = open(source, "r", encoding="utf-8")
    lines = file.read()
    file.close()

    for r in repl: lines = lines.replace(r[0], r[1])

    path = target[0:target.rindex('/')]
    if not os.path.exists(path): os.makedirs(path)
    file = open(target, "w", encoding="utf-8", newline='\n')
    file.write(lines)
    file.close()
