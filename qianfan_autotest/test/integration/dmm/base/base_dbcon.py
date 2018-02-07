# coding=utf-8
import pytest
import unittest
from libs.config import get_db_connection
from test.integration.dmm.api.base_dmm_login import BaseDMMTestCase


@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
class DBConnectionTest(BaseDMMTestCase):
    def setUp(self):
        super(DBConnectionTest, self).setUp()

    def tearDown(self):
        super(DBConnectionTest, self).tearDown()

    """验证DMM 数据库连接"""

    def test1(self):
        # assert get_db_connection('dmm')
        self.assertIsNotNone(self.mysql_conn)

    def test2(self):
        # assert get_db_connection('dmm','plat')
        self.assertIsNotNone(self.platmysql_conn)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
