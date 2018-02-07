#coding=utf-8
import os

import allure
import pytest
import requests
import xlrd

from libs.dmm.api.merchant import export
from test.integration.dmm.base.base_const import dmm_base_const
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase

@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@allure.feature('dmm开户管理—导出')
class MerchantExportTest(BaseDMMTestCase):
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
    @pytest.mark.serviceprovider
    @allure.story("1.开户管理—导出")
    def test_case1(self):
        """
        导出开户商户文件-无任何查询条件
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

            res = export(self.session, self.baseurl, query_cond)
            if res.status_code != 200:
                raise ValueError(res.text)
            json_data = res.json()
            r = requests.get(json_data['data'], stream=True)
            # 将URL中的文件下载到下面的目录中，当前文件目录
            filepath = os.path.join(os.path.dirname(__file__), 'dmm_merchant_dowmload.xlsx')
            with open(filepath, "wb") as code:
                code.write(r.content)
            # 打开导出的文件并读取文件行数
            data = xlrd.open_workbook(filepath)
            table = data.sheets()[0]
            lines = table.nrows - 1
            print('======api call result=====')
            print lines

            # 数据库查询
            sql1 = "SELECT ServiceProviderUser.uuid FROM ServiceProviderUser " \
                   "INNER JOIN ServiceProvider2 ON ServiceProvider2.uuid = ServiceProviderUser.serviceProvider " \
                   "WHERE (ServiceProviderUser.service = \"pay\") " \
                   "AND ((ServiceProviderUser.serviceProvider = \"%r\") " \
                   "OR (ServiceProvider2.upper = \"\"))" %dmm_base_const.fromServiceProvider
            sqlResult1 = self.query_db(sql1)
            # 计数，记录条数
            count = 0
            for userUuid in sqlResult1:
                sqlResult2 = None
                sql2 = 'SELECT UserPayChannel.uuid, UserPayChannel.version, UserPayChannel.created, UserPayChannel.creatorNS,' \
                       ' UserPayChannel.creatorId, UserPayChannel.creatorName, UserPayChannel.lastModified, UserPayChannel.lastModifierNS,' \
                       ' UserPayChannel.lastModifierId, UserPayChannel.lastModifierName, USER.mobile, USER.name , USER.idCard, USER.password,' \
                       ' USER.refundPwd, USER.enabled, USER.recommendedBy, USER.education, USER.lastLoginTime, USER.lastLoginIp, USER.secondLastLoginTime,' \
                       ' USER.secondLastLoginIp, USER.remark, USER.storageId, USER.verifiedFields, tenant.uuid AS tenantUUID, tenant.name AS tenantName,' \
                       ' UserPayChannel.user, UserPayChannel.payment, UserPayChannel.channel, UserPayChannel.payConfig, UserPayChannel.materialConfig,' \
                       ' UserPayChannel.openState, UserPayChannel.openFailCause, UserPayChannel.worksheetState, UserPayChannel.worksheetNum,' \
                       ' UserPayChannel.channelId, UserPayChannel.channelRate, UserPayChannel.openSource, UserPayChannel.salesman ' \
                       'FROM UserPayChannel	' \
                       'INNER JOIN USER ON USER.uuid = UserPayChannel.user ' \
                       'LEFT JOIN tenant ON tenant.user = UserPayChannel.user ' \
                       'WHERE UserPayChannel.payment IN (\'micropay\')AND UserPayChannel.user IN (\'%s\')' % userUuid
                sqlResult2 = self.query_platdb(sql2)
                if len(sqlResult2) != 0:
                    count = count + 1
            print('======sql result=====')
            print(count)

            self.assertEqual(lines, count)
        except Exception as e:
            self.fail(e.message)


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
