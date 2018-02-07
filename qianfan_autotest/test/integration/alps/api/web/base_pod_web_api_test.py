# coding=utf-8
import unittest
import requests

from libs.config import get_baseurl, get_db_connection
from libs.dmm.api.auth import login, logout
from libs.dmm.api.models import BLogin


class BaseAlpsTestCase(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.baseurl = get_baseurl('alps')
        # do login
        self.bloc = '0000'
        self.data = {
            "userCode": "admin",
            "password": "888888",
            "orgUuid": "0003"
        }
        res = login(self.session, self.baseurl, self.bloc, self.data)
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        res = logout(self.session, self.baseurl, self.bloc)
        self.assertEqual(res.status_code, 200)
