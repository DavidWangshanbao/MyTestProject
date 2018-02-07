# coding=utf-8
import allure
import pytest
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.employee_h4 import EmployeeH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4


@pytest.mark.employee_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '员工管理', '员工']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"员工-汇总"页面'):
        HomeH4.verify_page_opened(driver, '员工-汇总')
    with allure.step('新增员工'):
        code = '1024'
        name = u'木子'
        password = '123456'
        confirm_password = '123456'
        EmployeeH4.create_employee(driver, code, name, password, confirm_password)
