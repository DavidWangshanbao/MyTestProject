#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import time


def wait_for(times):
    time.sleep(times)


def highlight(driver, element):
    """Highlights (blinks) a Selenium Webdriver element"""
    # driver = element._parent
    def apply_style(driver, element, s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
    original_style = element.get_attribute('style')
    apply_style(driver, element, "background: yellow; border: 2px solid red;")
    # time.sleep(.3)
    # apply_style(original_style)