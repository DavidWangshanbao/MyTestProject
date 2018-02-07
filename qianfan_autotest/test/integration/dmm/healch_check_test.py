# coding=utf-8
import allure
import pytest
import unittest

import requests

from libs.config import get_baseurl
from libs.dmm.api.health import health_check

@allure.feature('dmm')
@pytest.mark.dmm
@pytest.mark.dmm_api
@pytest.mark.api
@pytest.mark.smoke
class HealthCheckTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.baseurl = get_baseurl('dmm')

    @allure.story("healthcheck")
    def test_health(self):
        res = health_check(self.session, self.baseurl)
        if res.status_code != 200:
            raise ValueError(res.text)
        json_data = res.json()
        assert json_data.get('state') == 1


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
