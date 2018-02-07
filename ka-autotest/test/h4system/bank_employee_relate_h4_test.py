# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.bank_account_h4 import BankAccountH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4

"""
维护银行账户与员工关系，并添加银行账户数据
"""


@pytest.mark.bank_employee_relate_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['财务管理', '基础设置', '银行账户档案维护']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"银行账户档案维护-明细"页面'):
        HomeH4.verify_page_opened(driver, '银行账户档案维护-明细')
    with allure.step('维护银行账户与员工关系'):
        BankAccountH4.relate_bank_employee(driver, u'门店缴款')
    with allure.step('返回银行账户档案维护页面'):
        BankAccountH4.back_to_account(driver)
    with allure.step('添加银行账户档案数据'):
        list_name = ['代码', '中文名称', '财务代码', '用途']
        list_value = ['1024', u'农业133', '023', u'门店缴款']
        BankAccountH4.add_new_data(driver, list_name, list_value)
    with allure.step('退出登陆'):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()


