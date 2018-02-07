# coding=utf-8
# -*- coding: UTF-8 -*-
from datetime import datetime
from datetime import timedelta
import pytest

from libs.dmm.api.serviceprovider.device import query
from test.integration.dmm.api.base_const import dmm_base_const
from test.integration.dmm.api.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
class ServiceProviderDeviceQueryTest(BaseDMMTestCase):
    def setUp(self):
        super(ServiceProviderDeviceQueryTest, self).setUp()

    def tearDown(self):
        super(ServiceProviderDeviceQueryTest, self).tearDown()

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
        设备管理：无查询条件
        :return:
        """
        try:
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": ""
                },
                {
                    "property": "serviceProviderName:%=%",
                    "value": ""
                },
                {
                    "property": "date:[,]",
                    "value": [None, None]
                },
                {
                    "property": "merchantName:%=%",
                    "value": ""
                },
                {
                    "property": "shopSortName:%=%",
                    "value": ""
                },
                {
                    "property": "state:=",
                    "value": ""
                },
                {
                    "property": "healthState:=",
                    "value": ""
                },
                {
                    "property": "serviceProvider:=",
                    "value": ""
                }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(len(json_data.get('data')))
            sql = "SELECT uuid FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' OR parentServiceProvider = \'" + dmm_base_const.fromServiceProvider + "\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case2(self):
        """
         设备管理：服务商ID
         :return:
         """
        try:
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": ""
                },
                    {
                        "property": "serviceProviderName:%=%",
                        "value": ""
                    },
                    {
                        "property": "date:[,]",
                        "value": [None, None]
                    },
                    {
                        "property": "merchantName:%=%",
                        "value": ""
                    },
                    {
                        "property": "shopSortName:%=%",
                        "value": ""
                    },
                    {
                        "property": "state:=",
                        "value": ""
                    },
                    {
                        "property": "healthState:=",
                        "value": ""
                    },
                    {
                        "property": "serviceProvider:=",
                        "value": dmm_base_const.toServiceProvider
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(len(json_data.get('data')))
            sql = "SELECT uuid FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.toServiceProvider \
                  + "\' OR parentServiceProvider = \'" + dmm_base_const.toServiceProvider + "\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case3(self):
        """
          设备管理：一级或二级服务商名称
          :return:
          """
        try:
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": ""
                },
                    {
                        "property": "serviceProviderName:%=%",
                        "value": dmm_base_const.toServiceProviderName
                    },
                    {
                        "property": "date:[,]",
                        "value": [None, None]
                    },
                    {
                        "property": "merchantName:%=%",
                        "value": ""
                    },
                    {
                        "property": "shopSortName:%=%",
                        "value": ""
                    },
                    {
                        "property": "state:=",
                        "value": ""
                    },
                    {
                        "property": "healthState:=",
                        "value": ""
                    },
                    {
                        "property": "serviceProvider:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(len(json_data.get('data')))
            sql = "SELECT UUID FROM serviceprovider2 WHERE NAME = \'" + dmm_base_const.toServiceProviderName \
                  + "\' AND upper = \'" + dmm_base_const.fromServiceProvider + "\'"
            res = self.query_db(sql)
            serviceProviderUuid = res[0][0]
            sql = "SELECT uuid FROM serviceproviderdevice WHERE serviceProvider = \'" + serviceProviderUuid \
                  + "\' OR parentServiceProvider = \'" + serviceProviderUuid + "\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case4(self):
        """
        设备分配时间查询：暂定查询一个月
        :return:
        """
        try:
            quert_time_start = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            quert_time_end = datetime.now().strftime('%Y-%m-%d')
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": ""
                },
                    {
                        "property": "serviceProviderName:%=%",
                        "value": ""
                    },
                    {
                        "property": "date:[,]",
                        "value": [quert_time_start, quert_time_end]
                    },
                    {
                        "property": "merchantName:%=%",
                        "value": ""
                    },
                    {
                        "property": "shopSortName:%=%",
                        "value": ""
                    },
                    {
                        "property": "state:=",
                        "value": ""
                    },
                    {
                        "property": "healthState:=",
                        "value": ""
                    },
                    {
                        "property": "serviceProvider:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(len(json_data.get('data')))
            sql = "SELECT uuid FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' OR parentServiceProvider = \'" + dmm_base_const.fromServiceProvider + "\'" + " AND assignTime between \'" \
                  + quert_time_start + "\' AND \'" + quert_time_end + "\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case5(self):
        """
        盒子状态查询：已分配
        :return:
        """
        try:
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": ""
                },
                    {
                        "property": "serviceProviderName:%=%",
                        "value": ""
                    },
                    {
                        "property": "date:[,]",
                        "value": ""
                    },
                    {
                        "property": "merchantName:%=%",
                        "value": ""
                    },
                    {
                        "property": "shopSortName:%=%",
                        "value": ""
                    },
                    {
                        "property": "state:=",
                        "value": "assigned"
                    },
                    {
                        "property": "healthState:=",
                        "value": ""
                    },
                    {
                        "property": "serviceProvider:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(len(json_data.get('data')))
            sql = "SELECT uuid FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' OR parentServiceProvider = \'" + dmm_base_const.fromServiceProvider + "\'" + "AND state = \'assigned\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case6(self):
        """
        设备状态：正常
        :return:
        """
        try:
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": ""
                },
                    {
                        "property": "serviceProviderName:%=%",
                        "value": ""
                    },
                    {
                        "property": "date:[,]",
                        "value": ""
                    },
                    {
                        "property": "merchantName:%=%",
                        "value": ""
                    },
                    {
                        "property": "shopSortName:%=%",
                        "value": ""
                    },
                    {
                        "property": "state:=",
                        "value": ""
                    },
                    {
                        "property": "healthState:=",
                        "value": "true"
                    },
                    {
                        "property": "serviceProvider:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(len(json_data.get('data')))
            sql = "SELECT uuid FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' OR parentServiceProvider = \'" + dmm_base_const.fromServiceProvider + "\'" + "AND healthstate = \'1\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case7(self):
        """
        设备id
        :return:
        """
        try:
            sql = "SELECT deviceId FROM serviceproviderdevice WHERE serviceProvider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' OR parentServiceProvider = \'" + dmm_base_const.fromServiceProvider + "\'"
            res = self.query_db(sql)
            deviceId = res[0][0]
            query_cond = {
                "filters": [{
                    "property": "deviceId:%=%",
                    "value": deviceId
                },
                    {
                        "property": "serviceProviderName:%=%",
                        "value": ""
                    },
                    {
                        "property": "date:[,]",
                        "value": ""
                    },
                    {
                        "property": "merchantName:%=%",
                        "value": ""
                    },
                    {
                        "property": "shopSortName:%=%",
                        "value": ""
                    },
                    {
                        "property": "state:=",
                        "value": ""
                    },
                    {
                        "property": "healthState:=",
                        "value": ""
                    },
                    {
                        "property": "serviceProvider:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }],
                # "start": 0,
                # "limit": 10
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)

        except Exception as e:
            self.fail(e.message)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
