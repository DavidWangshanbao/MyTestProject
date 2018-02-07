#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from libs.hdcard.ui.common.selectlist import SelectList
from libs.hdcard.ui.common.radio import Radio
from utils.commons import *


def createShoppingScore(driver, user, rewardType, beginTime, endTime, totalTimes, code1, score1, code2,
                        dprice2, score2, dayTimes=None):
    """
    创建商品积分兑奖规则
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param rewardType: 兑奖类型
    :param beginTime: 生效起始日期
    :param endTime: 生效结束日期
    :param dayTimes: 每日最大兑奖次数
    :param totalTimes: 最大兑奖次数
    :param code1: 第一个输入码
    :param score1: 第一个商品积分明细
    :param code2: 第二个输入码
    :param dprice2: 第二个抵扣价
    :param score2: 第二个商品积分明细
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "积分规则", "商品积分兑奖规则")
    wait_for(1)
    Button.click(driver, "新建")
    wait_for(1)
    Radio.set(driver, rewardType)
    TextBox.setValue(driver, "生效日期", beginTime)

    ####need to do####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//div[text()="生效日期"]/../..//tr/td[2]//input')
    element.send_keys(endTime)
    driver.switch_to_default_content()
    if dayTimes != None:
        TextBox.setValue(driver, "每日最大兑奖次数", dayTimes)
    TextBox.setValue(driver, "最大兑奖次数", totalTimes)

    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath(
        '//table[@class="rb-Form rb-Form-labelAlignRight"]//td[@class="rbi-Form-fieldCell"]/table/tbody/tr[2]/td[1]/div/input')
    element.send_keys(code1)
    element = driver.find_element_by_xpath(
        '//table[@class="rb-Form rb-Form-labelAlignRight"]//td[@class="rbi-Form-fieldCell"]/table/tbody/tr[2]/td[10]/div/input')
    element.send_keys(0)
    wait_for(1)
    element = driver.find_element_by_xpath(
        '//table[@class="rb-Form rb-Form-labelAlignRight"]//td[@class="rbi-Form-fieldCell"]/table/tbody/tr[2]/td[13]/table/tbody/tr/td[3]/div/input')
    element.send_keys(score1)

    element = driver.find_element_by_xpath('//img[@src="images/action/addItem-small.gif"]')
    element.click()

    element = driver.find_element_by_xpath(
        '//table[@class="rb-Form rb-Form-labelAlignRight"]//td[@class="rbi-Form-fieldCell"]/table/tbody/tr[3]/td[1]/div/input')
    element.send_keys(code2)
    element = driver.find_element_by_xpath(
        '//table[@class="rb-Form rb-Form-labelAlignRight"]//td[@class="rbi-Form-fieldCell"]/table/tbody/tr[3]/td[10]/div/input')
    element.send_keys(dprice2)
    element = driver.find_element_by_xpath(
        '//table[@class="rb-Form rb-Form-labelAlignRight"]//td[@class="rbi-Form-fieldCell"]/table/tbody/tr[3]/td[13]/table/tbody/tr/td[3]/div/input')
    element.send_keys(score2)
    driver.switch_to_default_content()

    Button.click(driver, "保存并审核")
    wait_for(2)
    Button.click(driver, "确定")
    assert Message.get_message(driver) == '保存并审核商品积分兑奖规则成功! '
