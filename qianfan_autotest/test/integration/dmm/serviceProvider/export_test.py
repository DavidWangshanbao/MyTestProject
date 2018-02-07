# coding=utf-8
# -*- coding: UTF-8 -*-
import os

import allure
import pytest
import requests
import xlrd

from libs.dmm.api.serviceprovider import export
from test.integration.dmm.base.base_const import dmm_base_const
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@pytest.mark.serviceprovider
@allure.feature('dmm服务商管理-导出')
class ServiceProviderExportTest(BaseDMMTestCase):
    def setUp(self):
        super(ServiceProviderExportTest, self).setUp()

    def tearDown(self):
        super(ServiceProviderExportTest, self).tearDown()

    def query_db(self, sql):
        res = []
        with self.mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        return res

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case1(self):
        """
        导出服务商文件，检验数据库符合条件的服务商条数是否和文件导出一致
        :return:
        """
        try:
            query_cond = {
                "start": 0,
                "limit": 100,
                "filters": [{
                    "property": "keywords:%=%",
                    "value": ""
                },
                    {
                        "property": "level:=",
                        "value": ""
                    },
                    {
                        "property": "mobile:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }]
            }
            res = export(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            r = requests.get(json_data['data'], stream=True)
            # 将URL中的文件下载到下面的目录中，当前文件目录
            filepath = os.path.join(os.path.dirname(__file__), 'dmm_devices_dowmload.xlsx')
            with open(filepath, "wb") as code:
                code.write(r.content)
            # 打开导出的文件并读取文件行数
            data = xlrd.open_workbook(filepath)
            table = data.sheets()[0]
            lines = table.nrows - 1
            print('======api call result=====')
            print lines

            # 数据库查询
            sql = "SELECT * FROM serviceprovider2 WHERE upper = \'" + dmm_base_const.fromServiceProvider + \
                  "\'ORDER BY created DESC LIMIT 10"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(lines, len(res))
        except Exception as e:
            self.fail(e.message)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
