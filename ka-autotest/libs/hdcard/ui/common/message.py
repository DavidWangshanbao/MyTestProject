#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


class Message(object):
    @classmethod
    def get_message(cls, driver):
        """
        获取操作后的提示信息
        :param driver: Selenium driver
        :return: 返回提示的具体信息
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath('//div[@class="gwt-HTML message"]')
        info = element.text
        driver.switch_to_default_content()
        return info