#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from utils.commons import *


def receiveCard(driver, user, billNumber, receiveCardCount, beginCardNo, endCardNo):
    """
     收卡
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :param billNumber:  定卡生成的单号
    :param receiveCardCount: 收货数量
    :param beginCardNo: 起始卡号
    :param endCardNo: 截至卡号
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "采购", "收卡")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "定卡单单号", billNumber)
    TextBox.setValue(driver, "收货数量", "")
    TextBox.setValue(driver, "收货数量", receiveCardCount)
    TextBox.setValue(driver, "起始卡号", beginCardNo)
    TextBox.setValue(driver, "截至卡号", "") #截至卡号会根据卡数量和起始卡号自动生成
    Button.click(driver, "添加")
    wait_for(1)

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[5]//div[text()="删除"]/../../../td[3]')
    assert element.text.find(beginCardNo) != -1
    driver.switch_to_default_content()

    Button.click(driver, "保存并审核")
    wait_for(1)
    Button.click(driver, "确定")
    wait_for(1)
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbe-bodybg"]')
    assert element.text.find(billNumber) != -1
    assert element.text.find("已审核") != -1
    driver.switch_to_default_content()

