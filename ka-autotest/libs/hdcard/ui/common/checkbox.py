#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


class CheckBox(object):
    @classmethod
    def set(cls, driver, object):
        """
        选择复选框类型的控件
        :param driver: Selenium driver
        :param object: 对应对象
        :return: 
        """
        if not CheckBox().is_checked(driver, object):
            driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
            element = driver.find_element_by_xpath(
                '//td[text()="{}"]/..//div[contains(@class, "rb-CheckBox")]'.format(object))
            element.click()
        driver.switch_to_default_content()

    @classmethod
    def clear(cls, driver, object):
        """
        清楚复选框选择
        :param driver: Selenium driver
        :param object: 对应对象
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath(
            '//td[text()="{}"]/..//div[contains(@class, "rb-CheckBox")]'.format(object))
        if CheckBox().is_checked(driver, object):
            element.click()
        driver.switch_to_default_content()

    def is_checked(self, driver, object):
        """
        判断复选框是否已选择
        :param driver: Selenium driver
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath(
            '//td[text()="{}"]/..//div[contains(@class, "rb-CheckBox")]'.format(object))
        attribute = element.get_attribute('outerHTML')
        driver.switch_to_default_content()
        if attribute.find("checkedHover") != -1:
            return True
        return False

