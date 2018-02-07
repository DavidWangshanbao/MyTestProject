#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


class TextBox(object):
    @classmethod
    def setValue(cls, driver, object, value):
        """
        操作文本框
        :param driver: Selenium driver
        :param object: 文本框对应的名称
        :param value: 输入的文本内容
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath('//div[text()="{}"]/../..//input'.format(object))
        from selenium.webdriver.common.action_chains import *
        from selenium.webdriver.common.keys import *
        ActionChains(driver).move_to_element(element).click().perform()
        import time
        time.sleep(1)
        element.send_keys(value)
        driver.switch_to_default_content()