#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


class Button(object):
    @classmethod
    def click(cls, driver, text):
        """
        操作页面button类型的控件
        :param driver: Selenium driver
        :param text: 控件的文本内容
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath('//div[@class="caption"][text()="{}"]'.format(text))
        element.click()
        driver.switch_to_default_content()
