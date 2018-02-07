#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from libs.hdcard.ui.common.checkbox import CheckBox
from utils.commons import *


def leadOutCard(driver, user, receivingUnit, receivingShop, boxes=[]):
    """
     领出卡
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "配送", "卡领出")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "收货单位", receivingUnit)
    TextBox.setValue(driver, "收货门店", receivingShop)
    click(driver, "筛选")
    wait_for(1)
    for x in boxes:
        checkbox_select(driver, x)
    Button.click(driver, "确认")

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="contentRoot"]')
    for x in boxes:
        assert element.text.find(x) != -1
    driver.switch_to_default_content()
    wait_for(1)
    Button.click(driver, "保存并审核")
    wait_for(1)
    Button.click(driver, "是")


def click(driver, object):
    """
    领出卡页面button操作
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//button[contains(text(),"{}")]'.format(object))
    element.click()
    driver.switch_to_default_content()


def checkbox_select(driver, object):
    """
    领出卡页面复选框操作
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[text()="{}"]/../../..//div[@class="button"]'.format(object))
    element.click()
    driver.switch_to_default_content()