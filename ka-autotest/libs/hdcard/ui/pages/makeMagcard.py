#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from utils.commons import *


def makeMagcard(driver, user, cardType, cardCount, cardBeginNo, cardEndNo):
    """
     制发磁卡
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "9999"]
    :param cardType: 卡类型
    :param cardCount: 制发卡数量
    :param cardBeginNo: 卡号范围起始
    :param cardEndNo: 卡号范围截止
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "卡生产", "制发卡")
    setValue(driver, "卡类型", cardType)
    setValue(driver, "制发卡数量", cardCount)
    setValue(driver, "卡号范围", cardBeginNo) #卡号的范围会根据数量和起始号自动生成，所以只输入起始范围即可

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    driver.find_element_by_xpath('//label[text()="～"]').click()
    driver.switch_to_default_content()

    click(driver, "开始制发卡")
    wait_for(5)
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//div[@class="rb-MsgBox-message"]')
    assert element.text.find("保存成功") != -1
    Button.click(driver, "确定")


def setValue(driver, object, value):
    """
    制发卡页面文本框操作
    :param driver: Selenium driver
    :param object: 操作文本框对象
    :param value: 输入值
    :return: 
    """
    # for x in value:
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//label[contains(text(),"{}")]/following-sibling::*//input'.format(object))
    # if object == "卡号范围" and value.index(x) == 1:
    #     element = driver.find_element_by_xpath(
    #         '//label[text()="～"]/following-sibling::div[1]//input')
    from selenium.webdriver.common.action_chains import *
    from selenium.webdriver.common.keys import *
    ActionChains(driver).move_to_element(element).click().perform()
    import time
    time.sleep(0.5)
    element.send_keys(value)
    driver.switch_to_default_content()


def click(driver, object):
    """
    制发卡页面button操作
    :param driver: Selenium driver
    :param object: 操作对象
    :return: 
    """
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//button[contains(text(),"{}")]'.format(object))
    element.click()
    driver.switch_to_default_content()