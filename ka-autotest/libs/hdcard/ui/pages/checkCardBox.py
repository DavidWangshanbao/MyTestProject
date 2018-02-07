#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from libs.hdcard.ui.common.selectlist import SelectList
from utils.commons import *
from setPasswordForCard import checkbox_select


def checkCardBox(driver, user):
    """
     核卡装盒
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "盒管理", "核卡装盒")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "盒号", boxBeginNo)
    checkbox_select(driver, "按卡号顺序装盒")
    TextBox.setValue(driver, "起始卡号", cardBeginNo)
    TextBox.setValue(driver, "结束卡号", cardEndNo)

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[contains(text(), "待核卡装盒的卡号")]/font')
    assert element.text.find(cardBeginNo) != -1
    driver.switch_to_default_content()

    for x in begin...end:
        TextBox.setValue(driver, "卡号", cardBeginNo)

    Button.click(driver, "保存并审核")