# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4
from libs.h4system.ui_h4.page_h4.supplier_h4 import SupplierH4


@pytest.mark.supplier_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '供应商管理', '供应商']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"供应商-汇总"页面'):
        HomeH4.verify_page_opened(driver, '供应商-汇总')
    with allure.step('新建供应商'):
        supplier_id = "1025"
        supplier_name = u"供应商测试数据"
        statement = u"已合作"
        SupplierH4.create_supplier(driver, supplier_id, supplier_name, statement)
    with allure.step("关闭页面"):
        time.sleep(2)
        title_list = u"供应商-明细"
        HomeH4.close_page(driver, title_list)
    with allure.step("退出登录"):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()
