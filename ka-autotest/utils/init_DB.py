#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys, os
import cx_Oracle

"""
##sql脚本命名规范：##
    hdpos4.6数据库初始化脚本： hd40.sql
    卡中心门店商品资料： hdcardctn_shop.sql
    卡中心卡类型商品： hdcardctn_cardtype.sql
    卡中心终端同步： hdcardctn_terminal.sql
"""

def operateOracle(file):
    """
    连接数据库，并执行sql脚本
    :param file: sql脚本名称
    :return: 
    """
##### connection 1 #####
# tns=cx_Oracle.makedsn('172.17.12.22',1521,'HDPOS4')
# con=cx_Oracle.connect('hd40','hd40',tns)
##### connection 2 #####
# con = cx_Oracle.connect('hd40/hd40@172.17.12.22/HDPOS4')
##### connection 3 #####
    try:
        filename = file.split(".")[0]
        if filename.find("hd40") != -1:
            con = cx_Oracle.connect('hd40','hd40','HDPOS4')
        elif filename.find("hdcardcts") != -1:
            con = cx_Oracle.connect('hdcardcts','hdcardcts',"HDCARDS")
        elif filename.find("hdcardhqn") != -1:
            con = cx_Oracle.connect('hdcardhqn','hdcardhqn',"HDCARDN")
        elif filename.find("hdcardctn") != -1:
            con = cx_Oracle.connect('hdcardctn','hdcardctn',"HDCARDN")
        else: raise(u"Warning: 文件名不规范，请检查文件名！")

        print(con.version)
        ## sql = "select * from rbversioncontrol" 测试sql语句
        sql = readSqlScript(file)
        cr = con.cursor()
        cr.execute(sql)
        con.commit()
        #### fetch result
        # rs = cr.fetchall()
        # for x in rs:
        #     print(x)
    finally:
        #### Close all connections ####
        cr.close()
        con.close()
    print("######### Finished #########")

def findSqlScript():
    for root, sub_dirs, files in os.walk(".\sqlScript"):
        return files


def readSqlScript(file):
    with open(".\\sqlScript\\"+file) as data_file:
        results = data_file.read()

    if file.split(".")[0].find("hdcardctn") != -1:
        import re, time
        current_system_datetime = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        results = re.sub(r'current_system_datetime', current_system_datetime, results)
    return results


def runScript():
    files = findSqlScript()
    for file in files:
        print(file)
        operateOracle(file)

if __name__ == "__main__":
    runScript()