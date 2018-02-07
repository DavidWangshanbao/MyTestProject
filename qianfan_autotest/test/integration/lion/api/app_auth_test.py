# coding=utf-8
import unittest

import pytest
import requests

from libs.config import get_baseurl
from libs.lion.api.app.auth import login
from libs.lion.api.app.auth.v2 import login as v2_login
import allure

@allure.feature('lion')
@pytest.mark.lion
@pytest.mark.lion_api
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.dops
class AuthTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.baseurl = get_baseurl('lion')

    @allure.story('login')
    def test_login(self):
        res = login(self.session, self.baseurl, mobile='13333333333', password='bhqpasswd')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(self.session.cookies) > 0)

    @allure.story('login')
    def test_v2_login(self):
        res = v2_login(self.session, self.baseurl, mobile='13333333333', password='bhqpasswd')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(self.session.cookies) > 0)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
