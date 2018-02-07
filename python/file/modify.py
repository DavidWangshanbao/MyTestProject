#!/usr/bin/python
#coding=utf-8

import xlrd
import xlutils.copy

book = xlrd.open_workbook('test.xls', formatting_info=True)
wtbook = xlutils.copy.copy(book)
wtsheet = wtbook.get_sheet(0)
wtsheet.write(0, 0, 'Ok, changed!')
wtbook.save('test.xls')
