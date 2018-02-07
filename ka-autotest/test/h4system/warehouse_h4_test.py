#  coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4
from libs.h4system.ui_h4.page_h4.warehouse_h4 import WarehouseH4


@pytest.mark.warehouse_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '仓位管理', '仓位']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"仓位-明细"页面'):
        HomeH4.verify_page_opened(driver, '仓位-明细')
    with allure.step('新增仓位'):
        warehouse_id = "14"
        warehouse_name = u"仓位A14"
        store_id = "0001"
        WarehouseH4.create_warehouse(driver, warehouse_id, warehouse_name, store_id)
    with allure.step('新增仓位'):
        time.sleep(3)
        warehouse_id = "15"
        warehouse_name = u"仓位A15"
        store_id = "7894"
        WarehouseH4.create_warehouse(driver, warehouse_id, warehouse_name, store_id)
    with allure.step('验证仓位是否存在'):
        time.sleep(3)
        warehouse_list = ["【14】 仓位A14", "【15】 仓位A15"]
        WarehouseH4.verify_warehouse(driver, warehouse_list)
    with allure.step("关闭页面"):
        title = "仓位-明细"
        HomeH4.close_page(driver, title)
    with allure.step("退出登录"):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()
