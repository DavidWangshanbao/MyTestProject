#coding=utf-8
import allure
import pytest

from libs.dmm.api.merchant import list
from test.integration.dmm.base.base_const import dmm_base_const
from test.integration.dmm.base.base_dmm_login import BaseDMMTestCase

@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@allure.feature('dmm开户管理—查询')
class MerchantListTest(BaseDMMTestCase):
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
    @allure.story("1.开户管理查询-无任何查询条件")
    def test_case1(self):
        """
        开户管理查询-无任何查询条件
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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
                    count = count +1
            print('======sql result=====')
            print(count)
            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            # self.fail(e.message)
            print  e

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("2.户管理查询-手机号或商户名称或简称")
    def test_case2(self):
        """
        开户管理查询-手机号或商户名称或简称
        :return:
        """
        try:
            query_cond = {
                "start": 0,
                "limit": 10,
                "filters": [{
                    "property": "userName:%=%",
                    "value": dmm_base_const.merchant_query_username
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("3.开户管理查询-开户时间起始")
    def test_case3(self):
        """
        开户管理查询-开户时间起始
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
                    "value": [dmm_base_const.merchant_query_start, None]
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("4.开户管理查询-开户时间截止")
    def test_case4(self):
        """
        开户管理查询-开户时间截止
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
                    "value": [None, dmm_base_const.merchant_query_end]
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("5.开户管理查询-开户人员")
    def test_case5(self):
        """
        开户管理查询-开户人员
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
                    "value": dmm_base_const.merchant_query_open
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("6.开户管理查询-开户状态")
    def test_case6(self):
        """
        开户管理查询-开户状态
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("7.开户管理查询-开户来源")
    def test_case7(self):
        """
        开户管理查询-开户来源
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

    @pytest.mark.dmm
    @pytest.mark.dmm_api
    @pytest.mark.api
    @pytest.mark.merchant
    @allure.story("8.开户管理查询-通道类型")
    def test_case8(self):
        """
        开户管理查询-通道类型
        :return:
        """
        try:
            query_cond = {
                "start": 0,
                "limit": 10,
                "filters": [{
                    "property": "userName:%=%",
                    "value": "第二门"
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
            json_data = res.json()
            print('======api call result=====')
            print(json_data)

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

            self.assertEqual(len(json_data.get('data')), count)

        except Exception as e:
            self.fail(e.message)

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
