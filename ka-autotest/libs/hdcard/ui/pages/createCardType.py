#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
# from libs.hdcard.ui.common.checkbox import CheckBox
from libs.hdcard.ui.common.selectlist import SelectList
from utils.commons import *


def createCardType(driver, user, code, name, cardMedia, cardLength, validatedDays, cardAmount, cardLimitAmount):
    """
     创建卡类型
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :param code: 代码
    :param name: 名称
    :param cardMedia: 卡介质
    :param cardLength: 卡长度
    :param validatedDays: 有效天数
    :param cardAmount: 卡面额
    :param cardLimitAmount: 卡限额
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "资料", "卡类型")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "代码", code)
    TextBox.setValue(driver, "名称", name)
    wait_for(1)
    checkbox_select(driver, "会员功能")
    checkbox_select(driver, "储值功能")
    checkbox_select(driver, "积分功能")
    SelectList.select(driver, "卡介质", cardMedia)
    TextBox.setValue(driver, "卡号长度", cardLength)
    TextBox.setValue(driver, "有效天数", validatedDays)
    TextBox.setValue(driver, "卡面额", cardAmount)
    TextBox.setValue(driver, "卡限额", cardLimitAmount)
    wait_for(1)
    Button.click(driver, "保存")
    wait_for(1)
    Button.click(driver, "确定")

    assert Message.get_message(driver) == '保存卡类型成功! '


def checkbox_select(driver, object):
    """
    创建卡类型页面，复选框操作方法
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    if not is_checked(driver, object):
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath(
            '//div[contains(@class, "rb-CheckBox")]//div[contains(text(), "{}")]/preceding-sibling::div[@class="button"]'.format(object))
        element.click()
    driver.switch_to_default_content()


def is_checked(driver, object):
    """
    复选框判断是否已选择
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[contains(@class, "rb-CheckBox")]//div[contains(text(), "{}")]/preceding-sibling::div[@class="button"]'.format(object))
    attribute = element.get_attribute('outerHTML')
    driver.switch_to_default_content()
    if attribute.find("checked") != -1:
        return True
    return False