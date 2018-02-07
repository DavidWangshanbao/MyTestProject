#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from utils.commons import *


def createShoppingScoreRules(driver, user, code, name, beginTime, endTime, cardType, price, dprice, scoreNum):
    """
    商品积分消费规则
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param code: 代码
    :param name: 名称
    :param beginTime: 生效起始日期
    :param endTime: 生效截止日期
    :param cardType: 卡类型
    :param price: 金额
    :param dprice: 抵扣限额
    :param scoreNum: 积分
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "积分规则", "积分消费规则")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "代码", code)
    TextBox.setValue(driver, "名称", name)
    TextBox.setValue(driver, "生效时间", beginTime)
    ####need to do####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//div[text()="生效时间"]/../..//tr/td[2]//input')
    element.send_keys(endTime)
    driver.switch_to_default_content()

    TextBox.setValue(driver, "卡类型", cardType)
    TextBox.setValue(driver, "金额", price)
    wait_for(2)
    TextBox.setValue(driver, u"抵扣限额", dprice)

    TextBox.setValue(driver, "积分", scoreNum)
    Button.click(driver, "添加")

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[3]/div[text()="删除"]/../../td[1]')
    assert element.text == u"[-]系统默认"

    element = driver.find_element_by_xpath(
        '//table[@class="rbi-Grid-dataGrid"]/tbody/tr[@class="rbi-Grid-row rbi-Grid-firstRow"]/td[3]/div[text()="删除"]/../../td[2]')
    assert element.text == u"{}.00".format(scoreNum)
    driver.switch_to_default_content()

    Button.click(driver, "保存")

    assert Message.get_message(driver) == u"保存积分消费规则成功! "

