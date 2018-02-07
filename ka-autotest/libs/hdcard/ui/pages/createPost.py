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

def createPost(driver, user, code, name, postName, department):
    """
    新增【岗位】
    :param driver: Selenium driver
    :param user: 登录用户、密码、组织，如：["admin", "admin", "8888"]
    :param code: 代码
    :param name: 名称
    :param postName: 岗位名称
    :param department: 所属部门
    :return: 
    """
    LoginPage.login(driver, user[0], user[1], user[2])
    Navigator.navigate(driver, "组织", "岗位")
    Button.click(driver, "新建")
    SelectList.select(driver, "岗位类型", "[{}]{}".format(code, name))
    TextBox.setValue(driver, "所属部门", department)
    wait_for(1)
    from selenium.webdriver.common.action_chains import *
    from selenium.webdriver.common.keys import *
    ActionChains(driver).key_down(Keys.ENTER).send_keys('').key_up(Keys.ENTER).perform()
    wait_for(1)
    Button.click(driver, "保存")
    assert Message.get_message(driver) == '保存岗位"{}"成功。 '.format(postName)

