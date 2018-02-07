# coding=utf-8
from __future__ import unicode_literals, print_function
import unittest
from collections import OrderedDict
import toolz
import xlrd
import sys
import xlsxwriter
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')


class IDataset(OrderedDict):
    def __init__(self, *args, **kwds):
        super(IDataset, self).__init__(*args, **kwds)

    def get_table(self, name):
        return self.get(name)

    @property
    def tablenames(self):
        return self.keys()


class QianfanTestCase(unittest.TestCase):
    """

    """

    def load_xls(self, xlsBook):
        """
        读取Excel文件
        :param xlxBook:  Excel book
        :return: DataSet
        """
        dataset = IDataset()
        xlrd.Book.encoding = 'utf-8'
        book = xlrd.open_workbook(xlsBook)
        for sheet_name in book._sheet_names:
            sheet = book.sheet_by_name(sheet_name=sheet_name)
            headers = sheet.row_values(0)
            rows = []
            for index in range(1, sheet.nrows):
                row = dict(zip(headers, sheet.row_values(index)))
                rows.append(row)
            dataset[sheet_name] = rows

        return dataset

    def assert_datatable_equal(self, data_table1, data_table2, excluded_columns=None):
        """
        verify two data set equals
        :param data_table1: list[dict]
        :param data_table2: list[dict]
        :param excluded_columns: a list， 不需要做比较的列名
        :return:
        """
        if excluded_columns:
            self.assertIsInstance(excluded_columns, list)
            data_table1 = map(lambda x: toolz.dissoc(x, *excluded_columns), data_table1)
            data_table2 = map(lambda x: toolz.dissoc(x, *excluded_columns), data_table2)

        self.assertItemsEqual(data_table1, data_table2)
        # if (data_table1 and data_table2 is None) or (data_table1 is None and data_table2):
        #     self.fail("not equal")
        #
        # if (len(data_table1) != len(data_table2)):
        #     self.fail("the length of {} and {} is not equal".format(data_table1, data_table2))
        #
        # for d in data_table1:
        #     if d not in data_table2:
        #         self.fail("{} is not found in \n{}".format(d, data_table2))
        #         break
        # self.assertTrue(True)

    def write_xls(self,path='dmm_devices_download.xlsx'):
        """
        写入Excel文件
        :return:在unit目录下生成相应excel文件
        """

        # 文件放在path路径下
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()

        deviceId = long(("1" + datetime.now().strftime('%Y%m%d%H%M%S')).encode("utf-8"))
        expenses = (
            ["%r" %deviceId, "", "派派支付盒子", "在库"],
        )

        row = 0
        col = 0

        for id, a, type, state in (expenses):
            worksheet.write(row, col, id)
            worksheet.write(row, col + 1, a)
            worksheet.write(row, col + 2, type)
            worksheet.write(row, col + 3, state)
            row += 1

        workbook.close()
