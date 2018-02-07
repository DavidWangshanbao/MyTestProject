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


def addCardBox(driver, user, cardTypeCode, use, boxBeginNo):
    """
     新增卡盒
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :param cardTypeCode: 卡类型编号
    :param use: 用途
    :param boxBeginNo: 起始盒号
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "盒管理", "生成盒号")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "卡类型编号", cardTypeCode)
    SelectList.select(driver, "用途", use)

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//div[text()="起始盒号"]/parent::*/following-sibling::*/div/input')
    element.send_keys(boxBeginNo)
    driver.switch_to_default_content()

    Button.click(driver, "保存")

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-headerGrid"]/tbody/tr[1]/td[1]//div[contains(text(),"盒号")]/../../../../../../..//tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[1]')
    assert element.text.find(boxBeginNo) != -1
