#!/usr/bin/python
#coding=utf-8


from __future__ import print_function,unicode_literals
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
import  xlrd
import  datetime
def readxlsx():
    #filename = sys.argv[1]
    filename = '1.xls'
    try:
        xlb = xlrd.open_workbook(filename)
    except IOError:
        print("没有 %s 文件" % filename)
        return 1
    ##xlrd从execl读取的类型共有以下几种
    ctype = {0:"empty",1:"string",2:"number",3:"date",4:"boolean",5:"error"}
    sh = xlb.sheet_by_index(0)
    for col in range(sh.ncols):
        id = sh.cell(1,col).value
        id_type  = sh.cell(1,col).ctype
        print(id,ctype.get(id_type))
    ##注意读取的bool 为0或1，不是True或者False

    ##以下是读取后赋值到变量后的类型
    for rx in range(1,sh.nrows):
        valus = sh.row_values(rx)
        code = valus[0] #string
        name = valus[1] #string
        date = valus[2] #date
        id = valus[3]  # number
        is_open = valus[4] #bool
        data_value = xlrd.xldate_as_tuple(date, xlb.datemode)
        date_string = datetime.date(*data_value[:3]).strftime('%Y/%m/%d')
        print(u"原date值：",date,u"类型:",type(date))  ##读取后date变成了float类型了
        print("各元素类型：code:",type(code),"name:",type(name),"date:",type(date_string),"id",type(id),"is_open:",type(is_open))
        print("各元素值：",code, name, date_string,id,is_open)
        #注意日期变成了string类型


if __name__ == '__main__':
    readxlsx()
