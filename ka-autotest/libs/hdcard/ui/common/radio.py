#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


class Radio(object):
    @classmethod
    def set(cls, driver, text):
        """
        操作页面radio控件
        :param driver: Selenium driver
        :param text: radio控件对应的label文本内容
        :return: 
        """
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath('//label[text()="{}"]/preceding-sibling::input'.format(text))
        if not element.is_selected(): element.click()
        driver.switch_to_default_content()
