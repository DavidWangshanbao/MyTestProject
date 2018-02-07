#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import *
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from libs.hdcard.ui.common.checkbox import CheckBox
from libs.hdcard.ui.common.link import Link
from utils.commons import *

def createEmployee(driver, user, code, name, postType, center, shop):
    """
    新增【员工】
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param code: 代码
    :param name: 姓名
    :param postName: 岗位名称
    :param department: 所属部门
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "组织", "员工")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "代码", code)
    TextBox.setValue(driver, "姓名", name)
    Button.click(driver, "保存")
    wait_for(1)
    assert Message.get_message(driver) == '保存员工"[{}]{}"成功。 '.format(code, name)

    ####Need to do####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    #solution 1
    # driver.find_element_by_xpath('//table[@class="cb-content"]//div[@class="caption"][text()="编辑"]').send_keys(
    #     Keys.NULL)
    #solution 2
    # element = driver.find_element_by_xpath('//table[@class="cb-content"]//div[@class="caption"][text()="编辑"]')
    # element.location_once_scrolled_into_view
    #solution 3
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #solution 4
    # element = driver.find_element_by_xpath('//table[@class="cb-content"]//div[@class="caption"][text()="编辑"]')
    # while not element.is_displayed():
    #     driver.execute_script("arguments[0].scrollIntoView()", element)
    #     wait_for(1)
    #solution 5
    element = driver.find_element_by_xpath('//table[@class="cb-content"]/descendant::table[@class="captionBar"]/descendant::div[text()="编辑"]')
    ####Need to do####
    # from selenium.webdriver.common.action_chains import *
    # from selenium.webdriver.common.keys import *
    # num = 3
    # while not element.is_displayed() and num > 0:
    #     ActionChains(driver).key_down(Keys.TAB).send_keys('').key_up(Keys.TAB).perform()
    #     wait_for(1)
    #     num -= 1

    element.click()
    driver.switch_to_default_content()
    Button.click(driver, "添加...")
    wait_for(1)
    CheckBox.set(driver, center)
    CheckBox.set(driver, shop)
    Button.click(driver, "确认")
    ActionChains(driver).key_down(Keys.ALT).send_keys('s').key_up(Keys.ALT).perform()
    wait_for(1)

    ####Need to do####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//td[text()="{}"]'.format(center))
    element.click()
    driver.switch_to_default_content()

    Link.click(driver, "担任的岗位")
    ####担任的岗位页面--编辑####
    ActionChains(driver).key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
    wait_for(1)
    ####担任的岗位页面--添加####
    ActionChains(driver).key_down(Keys.ALT).send_keys('n').key_up(Keys.ALT).perform()
    wait_for(1)
    CheckBox.set(driver, postType)
    Button.click(driver, "确认")
    wait_for(1)
    ####担任的岗位页面--添加--保存####
    ActionChains(driver).key_down(Keys.ALT).send_keys('s').key_up(Keys.ALT).perform()
    wait_for(1)

    ####Need to do####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//td[text()="{}"]'.format(shop))
    element.click()
    driver.switch_to_default_content()
    Link.click(driver, "拥有的权限")
    ####拥有的权限--编辑####
    ActionChains(driver).key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
    wait_for(1)
    Button.click(driver, "允许")
    wait_for(1)
    Button.click(driver, "全部 允许")
    wait_for(1)
    ####拥有的权限--保存####
    ActionChains(driver).key_down(Keys.ALT).send_keys('s').key_up(Keys.ALT).perform()
    wait_for(5)
    Button.click(driver, "阅读并确认")

