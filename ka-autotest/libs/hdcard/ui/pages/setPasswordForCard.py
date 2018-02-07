#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from utils.commons import *


def setPasswordForCard(driver, user, cardNum, newPWD, confirmNewPWD):
    """
     给会员卡设置密码
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param cardNum: 卡号
    :param newPWD: 新密码
    :param confirmNewPWD: 确认新密码
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "卡维护", "修改密码")
    TextBox.setValue(driver, "卡号", cardNum)

    from selenium.webdriver.common.action_chains import *
    from selenium.webdriver.common.keys import *
    ActionChains(driver).key_down(Keys.ENTER).send_keys('').key_up(Keys.ENTER).perform()
    wait_for(1)
    clear(driver, "是否输入原始密码")
    TextBox.setValue(driver, "新密码", newPWD)
    TextBox.setValue(driver, "确认密码", confirmNewPWD)
    Button.click(driver, "保存")
    wait_for(1)
    Button.click(driver, "确定")
    wait_for(1)
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[@class="rb-MsgBox-message"]')
    assert element.text.find("保存成功") != -1
    driver.switch_to_default_content()
    Button.click(driver, "确定")


def checkbox_select(driver, object):
    """
    给会员卡设置密码页面，复选框操作方法
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    if not is_checked(driver, object):
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath(
            '//div[text()="{}"]/../..//div[contains(@class, "rb-CheckBox")]//div[contains(@class, "button")]'.format(
                object))
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
        '//div[text()="{}"]/../..//div[contains(@class, "rb-CheckBox")]//div[contains(@class, "button")]'.format(
            object))
    attribute = element.get_attribute('outerHTML')
    driver.switch_to_default_content()
    if attribute.find("checked") != -1:
        return True
    return False


def clear(driver, object):
    """
    复选框在选择的情况下清掉
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    if is_checked(driver, object):
        driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
        element = driver.find_element_by_xpath(
            '//div[text()="{}"]/../..//div[contains(@class, "rb-CheckBox")]//div[contains(@class, "button")]'.format(
                object))
        element.click()
        driver.switch_to_default_content()
