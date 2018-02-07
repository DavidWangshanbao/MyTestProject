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


def createGetCard(driver, user, employee, cardType):
    """
     卡领用
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "888801"]
    :param employee: 员工代码
    :param cardType: 卡类型，如："[1212]花卡"
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "配送", "员工领用")
    wait_for(1)
    Button.click(driver, "新建")
    TextBox.setValue(driver, "收货员工", employee)
    Button.click(driver, "筛选")
    CheckBox.set(driver, cardType)
    Button.click(driver, "确认")

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[14]/../td[4]//div[@class="gwt-HTML html"]')
    assert element.text.find(cardType) != -1
    driver.switch_to_default_content()

    ####选择对应的数据，勾选数据前面的复选框####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[text()="{}"]/../../..//div[contains(@class, "rb-CheckBox")]'.format(cardType))
    element.click()
    driver.switch_to_default_content()
    Button.click(driver, "保存并审核")
    wait_for(1)
    Button.click(driver, "确定")
    wait_for(1)
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[@class="rb-MsgBox-message"]')
    assert element.text == "保存审核员工领用成功!"
    Button.click(driver, "确定")
    driver.switch_to_default_content()
