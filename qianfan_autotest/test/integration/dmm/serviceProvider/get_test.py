# coding=utf-8
# -*- coding: UTF-8 -*-
import allure
import pytest

from libs.dmm.api.serviceprovider import query, get
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@allure.feature('服务商管理-详情')
class ServiceProviderGetTest(BaseDMMTestCase):
    def setUp(self):
        super(ServiceProviderGetTest, self).setUp()

    def tearDown(self):
        super(ServiceProviderGetTest, self).tearDown()

    # @pytest.mark.skip
    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.serviceprovider
    def test_case1(self):
        """
        进入服务商详细界面
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
            json_data = res.json()['data'][0]
            getServiceUuid = json_data.get("id")
            res = get(self.session, self.baseurl, getServiceUuid)
            self.assertEqual(res.status_code, 200)
            json_data = res.json()
            self.assertEqual(json_data.get('success'), True)

        except Exception as e:
            print e

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
