#!/usr/bin/python
#coding=utf-8

import re
import sys
import os
import shutil



def replace():
    os.chdir('d:\\jpos\docker\\release\\')
    project_name = sys.argv[1]
    if os.path.exists(project_name):
        print(u"该产品文件夹已存在，请删除后重试")
        return 1
        #shutil.rmtree(project_name)

    shutil.copytree('f:\\temp\\'+project_name,project_name)
    copylist = ['HDLicense.properties','dockerfile','docker']
    for i in copylist:
        shutil.copyfile('d:\\jpos\docker\\release\\hnabl\\'+i,project_name+'\\'+i)


    ####替换posboSettings.xml文件配置

    with open(project_name+"/posboSettings.xml","r") as fb:
        buf = fb.read()

    buf = re.sub(r'<url>\s*http://.*/pfs-server/bfapp/buffalo/pfs\s*</url>','<url>http://172.17.2.41:8680/pfs-server/bfapp/buffalo/pfs</url>',buf,re.M|re.I)
    buf = re.sub(r'<serverUrl>\s*http://.*/OTTER/rest\s*</serverUrl>','<serverUrl>http://172.17.2.41:8580/OTTER/rest</serverUrl>',buf,re.M|re.I)
    buf = re.sub(r'<url>\s*http://.*/OTTER\s*</url>','<url>http://172.17.2.41:8580/OTTER</url>',buf,re.M|re.I)
    buf = re.sub(r'<storeStockAdjustOrderService>\s*.*\s*</storeStockAdjustOrderService>', '', buf, re.M | re.I)
    with open(project_name+"/posboSettings.xml", "w") as fb:
        fb.write(buf)

    ####替换datasource.xml文件配置
    with open(project_name+"/datasource.xml","r") as fb:
        buf = fb.read()

    buf = re.sub(r'<property name="initialSize" value="\d*" />', '<property name="initialSize" value="10" />', buf,1,re.M | re.I)
    buf = re.sub(r'<property name="maxActive" value="\d*" />', '<property name="maxActive" value="50" />', buf,1,re.M | re.I)
    buf = re.sub(r'<property name="maxWait" value="\d*"></property>', '<property name="maxWait" value="10000"></property>', buf,1,re.M | re.I)

    ##数据库地址配置
    buf = re.sub(r'<property name="url" value="jdbc:oracle:thin:@.*', '<property name="url" value="jdbc:oracle:thin:@172.17.12.9:1521:pos4stanew" />', buf, re.M | re.I)
    buf = re.sub(r'<property name="username" value=".*" />', '<property name="username" value="hd40" />', buf, re.M | re.I)
    buf = re.sub(r'<property name="password" value=".*" />', '<property name="password" value="hd40" />', buf, re.M | re.I)


    ##otter地址配置
    buf = re.sub(r'<property name="serviceUrl" value="http://.*/OTTER/remoting/jposService" />', '<property name="serviceUrl" value="http://172.17.2.41:8580/OTTER/remoting/jposService" />', buf, re.M | re.I)
    buf = re.sub(r'<property name="serviceUrl" value="http://.*/OTTER/bfapp/buffalo/KaoSvc" />','<property name="serviceUrl" value="http://172.17.2.41:8580/OTTER/bfapp/buffalo/KaoSvc" />', buf,re.M | re.I)
    buf = re.sub(r'<property name="serviceUrl" value="http://.*/OTTER/remoting/jposPlaceService" />', '<property name="serviceUrl" value="http://172.17.2.41:8580/OTTER/remoting/jposPlaceService" />', buf, re.M | re.I)
    buf = re.sub(r'<property name="serviceUrl" value="http://.*/OTTER/remoting/jposCustomerService" />', '<property name="serviceUrl" value="http://172.17.2.41:8580/OTTER/remoting/jposCustomerService" />',buf, re.M | re.I)
    buf = re.sub(r'<property name="serviceUrl" value="http://.*/OTTER/remoting/jposProductSvrService" />', '<property name="serviceUrl" value="http://172.17.2.41:8580/OTTER/remoting/jposProductSvrService" />', buf, re.M | re.I)

    with open(project_name+"/datasource.xml","w") as fb:
        fb.write(buf)

    ##检查是否在安装列表中存在，并且在文件开头加上
    with open("d:\\jpos\\docker\\release\\REPRO", "r") as fb:
        pro_res = fb.read()
        if re.search(project_name+'\n',pro_res,re.M | re.I):
            print(u"该产品名称已经存在")
        else:
            with open("d:\\jpos\\docker\\release\\REPRO", "w") as fb:
                fb.write(project_name + '\n' + pro_res)


    print(u"完成")
    return 0


replace()





