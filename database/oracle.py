#!/usr/bin/python
#coding=utf-8


from __future__ import unicode_literals,print_function
import cx_Oracle
import xlrd

def connect():
    #连接
    db=cx_Oracle.connect("hd40/hd40@172.17.11.254:1521/xftest")
    # 获取游标
    c=db.cursor()
    return (db,c)

def query(c):
    # 执行SQL
    sql = "select * from test_wang"
    c.execute(sql)
    # 获取数据
    result = c.fetchall()
    print(result)

def insert(db,c,sql):
    # 执行SQL
    c.execute(sql)
    # 提交
    db.commit()


def close(db,c):
    # 关闭游标
    c.close()
    # 关闭连接
    db.close()

def readxlsx():
    #filename = sys.argv[1]
    filename = '1.xls'
    try:
        xlb = xlrd.open_workbook(filename)
    except IOError:
        print("没有 %s 文件" % filename)
        return 1
    sh = xlb.sheet_by_index(0)
    sqllist = []
    for rx in range(1,sh.nrows):
        valus = sh.row_values(rx)
        code = valus[0]
        name = valus[1]
        date = valus[2]
        # 读取excle日期类型需要进行特殊转换
        data_value = xlrd.xldate_as_tuple(date, xlb.datemode)  #获得时间格式的元组
        date_string = datetime.date(*data_value[:3]).strftime('%Y/%m/%d')  #格式化
        print(code,name,date_string)
        #
        sql = "insert into test_wang values('%s','%s')" %(code,name)
        sqllist.append(sql)
    return sqllist

if __name__ == '__main__':
    db,c = connect()
    sqllist = readxlsx()
    for sql in sqllist:
        insert(db,c,sql)
    query(c)
    close(db,c)
