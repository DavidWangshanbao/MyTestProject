# coding=utf-8
import allure
import pytest
import unittest

import requests
from toolz import get_in
from libs.config import get_baseurl
from libs.alps.api.web.auth import login, logout, getorg

@allure.feature('alps')
@pytest.mark.alps
@pytest.mark.api
@pytest.mark.alps_api
@pytest.mark.smoke
@pytest.mark.dops
class AuthTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.baseurl = get_baseurl('alps')
        self.bloc = '0000'
        self.body = {
            "userCode": "admin",
            "password": "888888",
            "orgUuid": "0003"
        }

    @allure.story('login')
    def test_login_logout_getorg(self):
        res = login(self.session, self.baseurl, self.bloc, self.body)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(self.session.cookies) > 0)
        res = logout(self.session, self.baseurl, self.bloc)
        self.assertEqual(res.status_code, 200)
        res = getorg(self.session, self.baseurl, self.body)
        self.assertEqual(res.status_code, 200)
        json_data = res.json()
        orgs = get_in(['data', 'orgs'], json_data)
        self.assertTrue(len(orgs) > 0)


if __name__ == '__main__':
    pytest.main([__file__, "-sv"])
