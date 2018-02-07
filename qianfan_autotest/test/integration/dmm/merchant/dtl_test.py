#coding=utf-8
import allure
import pytest

from libs.dmm.api.merchant import dtl, list
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@allure.feature('dmm开户管理—详情')
class MerchantDtlTest(BaseDMMTestCase):
    def query_db(self,sql):
        res = []
        with self.mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        return res

    def query_platdb(self,sql):
        res = []
        with self.platmysql_conn.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        return res

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("1.开户管理—详情")
    def test_case1(self):
        """
        查看开户详情
        :return:
        """
        try:
            query_cond = {
                "start": 0,
                "limit": 10,
                "filters": [{
                    "property": "userName:%=%",
                    "value": ""
                },
                    {
                        "property": "created:[,]",
                        "value": [None, None]
                    },
                    {
                        "property": "creator:=",
                        "value": ""
                    },
                    {
                        "property": "openState:=",
                        "value": ""
                    },
                    {
                        "property": "openSource:=",
                        "value": ""
                    },
                    {
                        "property": "payment:=",
                        "value": ""
                    }],
                "sorters": [{
                    "property": "created",
                    "direction": "desc"
                }]
            }
            res = list(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            merchantUuid = res.json()['data'][0].get("id")
            res = dtl(self.session, self.baseurl, merchantUuid)
            if res.status_code != 200:
                raise ValueError(res.text)

        except Exception as e:
            # self.fail(e.message)
            print  e

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])