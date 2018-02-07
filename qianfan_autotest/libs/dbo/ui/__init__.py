#coding=utf-8
from __future__ import unicode_literals
from libs.config import get_baseurl
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class BaseDBOUIPage(object):
    def __int__(self,driver):
        self.driver = driver
        self.baseurl = get_baseurl('dbo')

    def login(self,username='liangxinxia',password='54325000111',token='xx'):
        self.driver.get(self.baseurl)
        self.driver.find_element_by_model('user.userName').send_keys(username)
        self.driver.find_element_by_model('user.userPassword').send_keys(username)
        self.driver.find_element_by_model('user.userCommand').send_keys(username)
        self.driver.find_element_by_css_selector('button[ng-click="login(user.userName,user.userPassword,user.userCommand)"]').click()


    def logout(self):
        self.driver.find_element_by_css_selector('span[ng-click="logout()"]').click()


