# coding=utf-8
from __future__ import unicode_literals, print_function
import os
import pytest
from utils import QianfanTestCase
from pprint import pprint


@pytest.mark.unit
@pytest.mark.excel
class ExcelReaderTest(QianfanTestCase):
    def setUp(self):
        self.basedir = os.path.dirname(__file__)

    def test_write_excel(self):
        dataset = self.write_xls()


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
