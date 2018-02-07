#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from utils.commons import *


class Link(object):
    @classmethod
    def click(cls, driver, object):
        """
        选择下拉列表对应的值
        :param driver: Selenium driver
        :param object: 超链接的文本信息
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        dropdown = driver.find_element_by_xpath('//div[@class="rb-Hyperlink"][text()="{}"]'.format(object))
        dropdown.click()
        driver.switch_to_default_content()
