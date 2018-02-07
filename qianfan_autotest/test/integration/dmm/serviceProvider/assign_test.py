# coding=utf-8
# -*- coding: UTF-8 -*-
import os

import allure
import pytest
import requests

from libs.config import get_baseurl
from libs.dbo.api.login import login
from libs.dbo.api.serviceprovider import assign as dboAssign
from libs.dmm.api.serviceprovider import assign
from test.integration.dbo.api.base_dbo_const import dbo_base_const
from test.integration.dmm.base.base_const import dmm_base_const
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm_api
@pytest.mark.api
@pytest.mark.serviceprovider
@allure.feature('dmm.serviceProvider_assign')
class ServiceProviderAssignTest(BaseDMMTestCase):
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

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test1(self):
        try:
            # 写入一个设备导入文件
            filepath = os.path.join(os.path.dirname(__file__),'dbo_devices_upload.xlsx')
            self.write_xls(filepath)

            # 登录dbo
            session = requests.Session()
            baseurl = get_baseurl('dbo')
            user = dbo_base_const.login_user
            password = dbo_base_const.login_pwd
            token = dbo_base_const.login_token
            res = login(session, baseurl, user=user, token=token, password=password)

            # 登录dbo后上传文件为服务商分配设备
            target_id = dmm_base_const.fromServiceProvider
            res = dboAssign(session, baseurl, target_id, filepath)
            self.assertEqual(res.status_code, 200)
            json_data = res.json()
            self.assertEqual(json_data.get('success'), True)

            # 进入dmm
            self.baseurl = get_baseurl('dmm')
            # 数据库查询刚刚导入的设备uuid
            sql = "SELECT UUID FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' ORDER BY created DESC LIMIT 1"
            res = self.query_db(sql)
            if len(res) != 0:
                (deviceUuid,) = res[0]
                target_id = dmm_base_const.toServiceProvider
                deviceUuid = deviceUuid.encode("utf-8")
                deviceUuids = [deviceUuid]
                res = assign(self.session, self.baseurl, target_id, deviceUuids)
                self.assertEqual(res.status_code, 200)
                json_data = res.json()
                self.assertEqual(json_data.get('success'), True)
            else:
                print "no device"

        except Exception as e:
            self.fail(e.message)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
