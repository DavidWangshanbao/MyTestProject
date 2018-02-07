# coding=utf-8
from __future__ import unicode_literals


class LoginPage(object):
    @classmethod
    def login(cls, driver, user='admin', password='admin', orgnization='8888'):
        """
        :param driver: Selenium driver
        :param user: 帐号
        :param password: 密码
        :param orgnization: 组织
        :return: N/A
        """
        driver.find_element_by_css_selector('div.rb-TextBox input').send_keys(user)
        driver.find_element_by_css_selector('div.rb-PasswordBox input').send_keys(password)
        driver.find_element_by_css_selector('div.rb-ComboBox input').send_keys(orgnization)
        # driver.find_element_by_xpath('//div[@class="caption"][text()="登录"]').click()
        driver.find_element_by_css_selector('div.rb-ButtonBase').click()

    @classmethod
    def logout(cls, driver):
        driver.find_element_by_xpath('//td[@class="logout"]/div[text()="退出"]').click()
