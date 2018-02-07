#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libs.hdcard.ui.common.login import LoginPage
from libs.hdcard.ui.common.navigator import Navigator
from libs.hdcard.ui.common.button import Button
from libs.hdcard.ui.common.textbox import TextBox
from libs.hdcard.ui.common.message import Message
from libs.hdcard.ui.common.selectlist import SelectList
from utils.commons import *

def createPostType(driver, user, code, name, postType):
    """
    新增【岗位类型】
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param code: 代码
    :param name: 名称
    :param postType: 岗位名称
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "组织", "岗位类型")
    Button.click(driver, "新建")
    TextBox.setValue(driver, "代码", code)
    TextBox.setValue(driver, "名称", name)
    TextBox.setValue(driver, "岗位名称", postType)
    Button.click(driver, "保存")
    assert Message.get_message(driver) == '保存岗位类型"[{}]{}"成功。 '.format(code, name)

    ####Need to do####
    driver.switch_to_frame(driver.find_element_by_id("RWindow1"))
    element = driver.find_element_by_xpath('//table[@class="cb-content"]//div[@class="caption"][text()="编辑"]')
    element.click()
    driver.switch_to_default_content()

    Button.click(driver, "允许")
    wait_for(1)
    Button.click(driver, "全部 允许")
    wait_for(1)
    # Button.click(driver, "保存")
    ####Need to do####
    from selenium.webdriver.common.action_chains import *
    from selenium.webdriver.common.keys import *
    ActionChains(driver).key_down(Keys.ALT).send_keys('s').key_up(Keys.ALT).perform()
    ####Need to do####
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//div[@class="caption"][text()="阅读并确认"]'))
    # )
    wait_for(5)
    Button.click(driver, "阅读并确认")
