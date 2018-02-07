#coding=utf-8
import unittest
import requests

from libs.config import get_baseurl, get_db_connection
from libs.dmm.api.auth import login,logout
from libs.dmm.api.models import BLogin
from utils import QianfanTestCase


class BaseDMMTestCase(QianfanTestCase):
    def setUp(self):
        self.session = requests.Session()
        self.baseurl = get_baseurl('dmm')
        # do login
        o = BLogin(accountNo='10000160', password='000000', captchaId='87264452818357497837453105680274975245',
                   captcha='12')
        login(self.session, self.baseurl, o)
        self.mysql_conn = get_db_connection(subsystem='dmm',alias='dmm')
        self.platmysql_conn = get_db_connection(subsystem='dmm',alias='plat')

    def tearDown(self):
        res = logout(self.session,self.baseurl)
        if self.mysql_conn:
            self.mysql_conn.close()
        if self.platmysql_conn:
            self.platmysql_conn.close()
        self.assertEqual(res.status_code,200)