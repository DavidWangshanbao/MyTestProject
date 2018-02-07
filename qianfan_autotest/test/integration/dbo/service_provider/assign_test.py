# coding=utf-8
# -*- coding: UTF-8 -*-
import pytest

from libs.dbo.api.serviceprovider import assign
from test.integration.dbo.api.base_dbo_test import BaseDBOTestCase


@pytest.mark.dbo
@pytest.mark.dbo_api
@pytest.mark.api
@pytest.mark.serviceprovider
class ServiceProviderAssignTest(BaseDBOTestCase):
    def setUp(self):
        super(ServiceProviderAssignTest, self).setUp()

    def tearDown(self):
        super(ServiceProviderAssignTest, self).tearDown()

    def query_db(self, sql):
        res = []
        with self.mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        return res


    def test1(self):
        try:
            target_id = '10000158'
            filepath = r"E:\automation_dmm\test\unit\dbo_devices_auto.xlsx"

            res = assign(self.session, self.baseurl, target_id, filepath)
            self.assertEqual(res.status_code, 200)
            json_data = res.json()
            self.assertEqual(json_data.get('success'), True)
        except Exception as e:
            self.fail(e.message)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
