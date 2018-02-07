# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4
from libs.h4system.ui_h4.page_h4.store_staff_management_h4 import StoreStaffManagementH4

"""
门店员工管理
添加员工到门店
"""


@pytest.mark.store_staff_management_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.17.12.23:8580/hdpos4-web")
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '员工管理', '门店员工管理']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"门店员工管理-明细"页面'):
        HomeH4.verify_page_opened(driver, '门店员工管理-明细')
    with allure.step('添加员工到门店'):
        store_id = '1019'
        StoreStaffManagementH4.staff_related_store(driver, store_id)
    with allure.step('关闭页面'):
        title = "门店员工管理-明细"
        HomeH4.close_page(driver, title)
    with allure.step("退出登陆"):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()
