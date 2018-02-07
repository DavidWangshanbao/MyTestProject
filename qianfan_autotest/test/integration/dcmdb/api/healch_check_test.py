# coding=utf-8
import unittest

import allure
import pytest

from libs.config import get_baseurl
from libs.dcmdb.api.health import health_check

@allure.feature('dcmdb')
@pytest.mark.api
@pytest.mark.dcmdb
@pytest.mark.dcmdb_api
@pytest.mark.smoke
@pytest.mark.dops
class HealthCheckTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = get_baseurl('dcmdb')

    @allure.story("healthcheck")
    def test1(self):
        res = health_check(self.baseurl)
        self.assertEqual(res.status_code, 200)
        json_data = res.json()
        self.assertEqual(json_data.get('state'), 1)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
