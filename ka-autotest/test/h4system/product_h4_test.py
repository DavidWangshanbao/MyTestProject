# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4
from libs.h4system.ui_h4.page_h4.product_h4 import ProductH4


@pytest.mark.product_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, '1111', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '商品管理', '商品']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"商品-汇总"页面'):
        HomeH4.verify_page_opened(driver, '商品-汇总')
    with allure.step('验证是否打开"商品-汇总"页面'):
        HomeH4.verify_page_opened(driver, '商品-汇总')
    with allure.step('新增商品'):
        product_id = '10260001'
        product_name = u"南瓜饼"
        brand_id = "01"
        category_id = "090101"
        warehouse_id = "01"
        supplier_id = "1025"
        ship_way = u"P货-直配"
        retail_price = "10"
        member_price = "10"
        high_price = "12"
        low_price = "8"
        trade_price = '5'
        inventory_price = "5"
        purchase_price = "5"
        high_inventory = "9999"
        daily_product = 0
        ProductH4.create_product(driver, product_id, product_name, brand_id, category_id, warehouse_id,
                                 supplier_id, ship_way, retail_price, member_price, high_price, low_price,
                                 trade_price, inventory_price, purchase_price, high_inventory, daily_product)
    with allure.step('关闭页面'):
        title = "商品-明细"
        HomeH4.close_page(driver, title)
    with allure.step('退出登录'):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()
