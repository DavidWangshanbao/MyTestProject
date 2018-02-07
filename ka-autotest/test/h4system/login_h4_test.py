#  coding=utf-8
import pytest
import time
from selenium import webdriver
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.h4system.ui_h4.element_h4.bank_account_page_h4 import BankAccountPageH4
from libs.h4system.ui_h4.element_h4.home_page_h4 import HomePageH4, location_pre, location_follow
from libs.h4system.ui_h4.page_h4.bank_account_h4 import BankAccountH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4


# http://172.17.11.104:8080/hdpos4-web
# http://172.17.12.23:8580/hdpos4-web


@pytest.mark.login_h4
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










