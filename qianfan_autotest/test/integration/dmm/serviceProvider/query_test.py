# coding=utf-8
# -*- coding: UTF-8 -*-
import allure
import pytest

from libs.dmm.api.serviceprovider import query
from test.integration.dmm.base.base_const import dmm_base_const
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@allure.feature('dmm服务商管理-查询')
class ServiceProviderQueryTest(BaseDMMTestCase):
    def setUp(self):
        super(ServiceProviderQueryTest, self).setUp()

    def tearDown(self):
        super(ServiceProviderQueryTest, self).tearDown()

    def query_db(self, sql):
        res = []
        with self.mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        return res

    # @pytest.mark.skip
    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case1(self):
        """
        服务商查询：服务商
        :return:
        """
        try:
            query_cond = {
                "start": 0,
                "limit": 100,
                "filters": [{
                    "property": "keywords:%=%",
                    "value": dmm_base_const.toServiceProvider
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
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(json_data)
            sql = "SELECT * FROM serviceprovider2 WHERE upper = \'" +dmm_base_const.toServiceProvider + \
                  "\' AND ( UUID LIKE \'%" + dmm_base_const.toServiceProvider + \
                  "%\' OR NAME LIKE \'%" + dmm_base_const.toServiceProvider + \
                  "%\' OR shortName LIKE \'%"+ dmm_base_const.toServiceProvider+"%\') " \
                  "ORDER BY created DESC LIMIT 10"
            res = self.query_db(sql)
            print('======sql result=====')
            print(res)
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            print e

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case2(self):
        """
        服务商查询：级别
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
                        "value": dmm_base_const.merchent_query_level
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
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(json_data)
            sql = "SELECT * FROM serviceprovider2 WHERE upper = \'" +dmm_base_const.toServiceProvider + \
                  "\' AND LEVEL = \'" + dmm_base_const.merchent_query_level + \
                  "\'ORDER BY created DESC LIMIT 10"
            res = self.query_db(sql)
            print('======sql result=====')
            print(res)
            self.assertEqual(len(json_data.get('data')), len(res))
        except Exception as e:
            print e

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case3(self):
        """
        服务商查询：手机号
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
                        "value": dmm_base_const.merchent_query_mobile
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }]
            }
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(json_data)
            sql = "SELECT * FROM serviceprovider2 WHERE upper = \'" + dmm_base_const.toServiceProvider + \
                  "\' AND mobile = \'" + dmm_base_const.merchent_query_mobile + \
                  "\'ORDER BY created DESC LIMIT 10"
            res = self.query_db(sql)
            print('======sql result=====')
            print(res)
            self.assertEqual(len(json_data.get('data')), len(res))
        except Exception as e:
            print e

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case4(self):
        """
        无任务条件查询
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
            res = query(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            print('======api call result=====')
            print(json_data)
            sql = "SELECT * FROM serviceprovider2 WHERE upper = \'" + dmm_base_const.toServiceProvider + \
                  "\'ORDER BY created DESC LIMIT 10"
            res = self.query_db(sql)
            print('======sql result=====')
            print(res)
            self.assertEqual(len(json_data.get('data')), len(res))
        except Exception as e:
            print e

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
