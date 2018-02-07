#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from utils.commons import *


def createScoreForMemberCard(driver, user, shop, card, money):
    """
    后台消费给会员卡添加积分
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param shop: 消费门店
    :param card: 卡号
    :param money: 消费金额
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "储值管理", "后台消费")
    TextBox.setValue(driver, "消费门店", shop)
    TextBox.setValue(driver, "卡号", card)
    wait_for(1)
    TextBox.setValue(driver, "消费金额", money)
    wait_for(1)
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//div[text()="说明"]/../..//textarea')
    element.click()
    driver.switch_to_default_content()
    wait_for(1)
    Button.click(driver, "添加")
    wait_for(1)

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[1]')
    assert element.text.find(card) != -1

    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[6]')
    assert element.text.find("{}.00".format(money)) != -1

    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[7]')
    assert int(element.text) > 0
    driver.switch_to_default_content()

    Button.click(driver, "保存并审核")
    wait_for(1)
    Button.click(driver, "确定")
