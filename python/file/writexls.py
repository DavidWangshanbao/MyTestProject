#!/usr/bin/python
#coding=utf-8

import xlwt
#创建workbook对象
book = xlwt.Workbook(encoding='utf-8')
#增加sheet页
sheet = book.add_sheet('sheet_test', cell_overwrite_ok=True)
#在坐标(0,0)写入数据
sheet.write(0, 0, 'Python')
#获取指定行的row对象
row_data = sheet.row(0)
#对row对象的指定列写入数据
row_data.write(1, 'is')
#在坐标(0,2)写入数据
sheet.write(0, 2, 'very very useful.')
#设置行高
sheet.row(0).height = 1
#写入第二行数据
sheet.row(1).write(0,2017)
sheet.row(1).write(1,12)
sheet.row(1).write(2,28)
#设置列宽
sheet.col(2).width = 6000
#保存
book.save('test.xls')