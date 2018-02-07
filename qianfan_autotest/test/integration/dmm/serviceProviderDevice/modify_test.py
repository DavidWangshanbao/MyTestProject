# coding=utf-8
import pytest

from libs.dmm.api.serviceprovider.device import query, modify
from test.integration.dmm.api.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
class ServiceProviderDeviceQueryTest(BaseDMMTestCase):
    def setUp(self):
        super(ServiceProviderDeviceQueryTest, self).setUp()

    def tearDown(self):
        super(ServiceProviderDeviceQueryTest, self).tearDown()

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
            deviceId = res.json()['data'][0].get("id")
            modify_cond={
                "id": deviceId,
                "healthState": "false",
                "remark": None
            }
            res = modify(self.session, self.baseurl, modify_cond)
            self.assertEqual(res.status_code, 200)
            json_data = res.json()
            self.assertEqual(json_data.get('success'), True)

        except Exception as e:
            self.fail(e.message)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
