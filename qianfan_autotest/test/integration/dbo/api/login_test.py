# coding=utf-8
from __future__ import unicode_literals, print_function
import unittest

import allure
import pytest
import requests

from libs.config import get_baseurl
from libs.dbo.api.login import login, logout

@allure.feature('dbo')
@pytest.mark.api
@pytest.mark.dbo
@pytest.mark.dbo_api
@pytest.mark.smoke
@pytest.mark.dops
class DBOLoginTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.baseurl = get_baseurl('dbo')

    @allure.story('login')
    def test_login(self):
        user = 'liangxinxia'
        password = '54325000111'
        token = '2'
        response = login(self.session, self.baseurl, user=user, token=token, password=password)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(self.session.cookies) > 0)
        res = logout(self.session, self.baseurl)
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
