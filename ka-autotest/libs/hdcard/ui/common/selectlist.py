#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from utils.commons import *


class SelectList(object):
    @classmethod
    def select(cls, driver, object, value):
        """
        选择下拉列表对应的值
        :param driver: Selenium driver
        :param object: 下拉列表labletext
        :param value: 列表对应的值
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        dropdown = driver.find_element_by_xpath('//div[text()="{}"]/../..//input'.format(object))
        dropdown.click()
        wait_for(1)
        selectlist = driver.find_element_by_xpath('//div[@class="rb-ComboBoxDropdownItem"][text()="{}"]'.format(value))
        selectlist.click()
        wait_for(1)
        driver.switch_to_default_content()