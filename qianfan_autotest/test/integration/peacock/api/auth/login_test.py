# coding=utf-8
import unittest

import allure
import pytest

from libs.config import get_baseurl
from libs.mp.api.auth import login
import requests

@allure.feature('mp')
@pytest.mark.api
@pytest.mark.peacock
@pytest.mark.peacock_api
@pytest.mark.smoke
@pytest.mark.dops
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = get_baseurl('mp')
        self.session = requests.Session()

    @allure.story('login')
    def test1(self):
        res = login(self.session, self.baseurl, username='13333333333', password='bhqpasswd')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(self.session.cookies) > 0)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
