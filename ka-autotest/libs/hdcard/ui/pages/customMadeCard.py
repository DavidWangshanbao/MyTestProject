#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from utils.commons import *


def createCard(driver, user, provider, cardType, cardCount, beginCardNo, endCardNo):
    """
     定卡
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :param provider:  供应商
    :param cardType: 卡类型
    :param cardCount: 卡数量
    :param beginCardNo: 起始卡号
    :param endCardNo: 截至卡号
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "采购", "定卡")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "供应商", provider)
    TextBox.setValue(driver, "卡类型", cardType)
    TextBox.setValue(driver, "卡数量", cardCount)
    TextBox.setValue(driver, "起始卡号", beginCardNo)
    TextBox.setValue(driver, "截至卡号", "") #截至卡号会根据卡数量和起始卡号自动生成
    Button.click(driver, "添加")
    wait_for(1)

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[5]//div[text()="删除"]/../../../td[1]')
    assert element.text.find(cardType) != -1
    driver.switch_to_default_content()

    Button.click(driver, "保存并审核")
    wait_for(1)
    Button.click(driver, "确定")

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbe-bodybg"]')
    assert element.text.find(cardType) != -1
    assert element.text.find("已审核") != -1

    element = driver.find_element_by_xpath('//div[text()="单号"]/../..//div[@class="gwt-HTML html"]')
    generate_bill_number = element.text  #收卡页面需要这个生成的单号
    driver.switch_to_default_content()

    return generate_bill_number

