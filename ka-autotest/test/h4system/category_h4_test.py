# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.category_h4 import CategoryH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4


@pytest.mark.category_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '类别管理', '分类体系设定']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"分类体系设定"页面'):
        HomeH4.verify_page_opened(driver, '分类体系设定')
    with allure.step('新增一级类别'):
        category_id = "09"
        category_name = u"测试一级类别"
        product_amount = "999"
        CategoryH4.create_category(driver, category_id, category_name, product_amount)
    with allure.step('关闭页面'):
        title = "分类体系设定"
        HomeH4.close_page(driver, title)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '类别管理', '分类体系设定']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"分类体系设定"页面'):
        HomeH4.verify_page_opened(driver, '分类体系设定')
    with allure.step('新增二级类别'):
        category_id = "0901"
        category_name = u"测试二级类别"
        product_amount = "99"
        CategoryH4.create_category(driver, category_id, category_name, product_amount)
    with allure.step('关闭页面'):
        title = "分类体系设定"
        HomeH4.close_page(driver, title)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '类别管理', '分类体系设定']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"分类体系设定"页面'):
        HomeH4.verify_page_opened(driver, '分类体系设定')
    with allure.step('新增三级类别'):
        category_id = "090101"
        category_name = u"测试三级类别"
        product_amount = "9"
        CategoryH4.create_category(driver, category_id, category_name, product_amount)
    with allure.step('关闭页面'):
        title = "分类体系设定"
        HomeH4.close_page(driver, title)
    with allure.step('退出登录'):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()

