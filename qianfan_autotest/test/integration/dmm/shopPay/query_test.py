# coding=utf-8
# -*- coding: UTF-8 -*-
from datetime import datetime
from datetime import timedelta
import pytest

from libs.dmm.api.shop.pay import query
from test.integration.dmm.api.base_const import dmm_base_const
from test.integration.dmm.api.base_dmm_login import BaseDMMTestCase

@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
class ShopPayQueryTest(BaseDMMTestCase):
    def setUp(self):
        super(ShopPayQueryTest, self).setUp()

    def tearDown(self):
        super(ShopPayQueryTest, self).tearDown()

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
        支付推广-门店管理：无查询条件
        :return:
        """
        try:
            query_cond = {
                    "filters": [{
                        "property": "shopName:%=%",
                        "value": ""
                    },
                    {
                        "property": "ownerName:%=%",
                        "value": ""
                    },
                    {
                        "property": "ownerMobile:%=%",
                        "value": ""
                    },
                    {
                        "property": "enabledTime:[,]",
                        "value": [None]
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
            # service = '2'视为加盟关系
            sql = "SELECT * FROM serviceprovidershop WHERE	 serviceprovider = \'" + dmm_base_const.fromServiceProvider \
                  + "\' AND service = \'2\'"
            res = self.query_db(sql)
            print('======sql result=====')
            print(len(res))
            self.assertEqual(len(json_data.get('data')), len(res))

        except Exception as e:
            self.fail(e.message)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
