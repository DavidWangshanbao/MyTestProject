# coding=utf-8
from __future__ import unicode_literals
import sys
import os
import pytest
import allure

from selenium.webdriver import Chrome
# from selenium.webdriver import Ie

from libs.hdcard.ui.pages.createPostType import *
from libs.hdcard.ui.pages.createPost import *
from libs.hdcard.ui.pages.createEmployee import *
from libs.hdcard.ui.pages.createShoppingScore import *
from libs.hdcard.ui.pages.createScoreRules import *
from libs.hdcard.ui.pages.createScoreForMemberCard import *
from libs.hdcard.ui.pages.createShoppingScoreRules import *
from libs.hdcard.ui.pages.createProviders import *
from libs.hdcard.ui.pages.createCardType import *
from libs.hdcard.ui.pages.customMadeCard import *
from libs.hdcard.ui.pages.receiveCard import *
from libs.hdcard.ui.pages.createGetCard import *
from libs.hdcard.ui.pages.setPasswordForCard import *
from libs.hdcard.ui.pages.makeMagcard import *
from libs.hdcard.ui.pages.addCardBox import *
from libs.hdcard.ui.pages.leadOutCard import *
from utils.commons import *

reload(sys)
sys.setdefaultencoding('utf-8')
driver = None
login_url = os.getenv("HDCARD_WEB_URL", 'http://172.17.12.23:8680/card')


def setup_module(module):
    global driver
    print('suite setup')
    driver = Chrome()
    # driver = Ie()
    driver.get(login_url)
    driver.implicitly_wait(2)
    driver.maximize_window()


@pytest.mark.sample
def test():
    # assert 1 + 1, 2
    global driver
    try:
        # with allure.step(u"新增部门类型"):
        #     LoginPage.login(driver, "admin", "admin", "8888")
        #     Navigator.navigate(driver, "组织", "部门类型")
        #     Button.click(driver, "新建")
        #     Button.click(driver, "取消")
        #     # TextBox.setValue(driver, "代码 起始于", "auto3")
        #     Button.click(driver, "新建")
        #     TextBox.setValue(driver, "代码", "auto1")
        #     TextBox.setValue(driver, "名称", "auto2")
        #     Button.click(driver, "保存")
        #     assert Message.get_message(driver) == '保存部门类型"auto2[auto1]"成功。 '
        # with allure.step(u"新增部门"):
        #     wait_for(3)
        #     LoginPage.login(driver, "admin", "admin", "8888")
        #     Navigator.navigate(driver, "组织", "部门")
        #     Button.click(driver, "新建")
        #     TextBox.setValue(driver, "代码", "auto1")
        #     TextBox.setValue(driver, "名称", "auto2")
        #     SelectList.select(driver, "部门类型", "[1]部门A")
        #     Button.click(driver, "保存")
        #     assert Message.get_message(driver) == '保存部门"[auto1]auto2"成功。 '
        # with allure.step(u"新增-岗位类型"):
        #     createPostType(driver, ["admin", "admin", "8888"], "ljauto1", "ljauto2", "测试")
        # with allure.step(u"新增-岗位"):
        #     createPost(driver, ["admin", "admin", "8888"], "ljauto1", "ljauto2", "测试", "02")
        # with allure.step(u"新增-员工"):
        #     createEmployee(driver, ["admin", "admin", "8888"], "1010", "ljauto2", "岗位类型A", "8888", "888801")
        # with allure.step(u"新增-员工"):
        #     createShoppingScore(driver, ["admin", "admin", "8888"], "普通兑奖", "2017-10-20", "2017-10-23", 100, "12000012",
        #                         10, "15000026", 2, 10, 10)
        # with allure.step(u"创建积分规则"):
        #     createScoreRoles(driver, ["admin", "admin", "8888"], "2288", u"积分消费A", "2017-10-21", "2017-10-23", u"巧克力卡", 1, 50)
        # with allure.step(u"后台消费给会员卡添加积分"):
        #     createScoreForMemberCard(driver, ["admin", "admin", "8888"], "888801", "9999201712120001", 10)
        # with allure.step(u"商品积分消费规则"):
        #     createShoppingScoreRules(driver, ["admin", "admin", "8888"], "1017", u"德芙", "2017-10-21", "2017-10-23", "德芙卡", 1, 1000, 1)
        # with allure.step(u"创建供应商"):
        #     createProviders(driver, ["admin", "admin", "9999"], "123455", "供应商A")
        # with allure.step(u"创建卡类型"):
        #     createCardType(driver, ["admin", "admin", "9999"], "1111", "德芙卡", "磁卡", 16, 3650, 500, 1000)
        # with allure.step(u"定卡"):
        #     createCard(driver, ["admin", "admin", "9999"], "6666", "1111", 5, "9999201711110001", "9999201711110005")
        # with allure.step(u"收卡"):
        #     receiveCard(driver, ["admin", "admin", "9999"], "9999171023000006", 1, "9999201711130001", "9999201711130001")
        # with allure.step(u"卡领用"):
        #     createGetCard(driver, ["admin", "admin", "888801"], "1221", "[1212]花卡")
        # with allure.step(u"给会员卡设置密码"):
        #     setPasswordForCard(driver, ["admin", "admin", "888801"], "9999201713130001", "123456", "123456")
        # with allure.step(u"制发磁卡"):
        #     makeMagcard(driver, ["admin", "admin", "9999"], "1111", 4, "9999201714140001", "9999201714140004")
        # with allure.step(u"新增卡盒"):
        #     addCardBox(driver, ["admin", "admin", "9999"], "1111", "发售", "88880003")
        with allure.step(u"领出卡"):
            leadOutCard(driver, ["admin", "admin", "9999"], "8888", "888801", ["990001","990002"])
    finally:
        pass
        # driver.quit()
