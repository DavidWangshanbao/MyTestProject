# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.brand_maintain_h4 import BrandMaintainH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4

"""
品牌维护
"""


@pytest.mark.brand_maintain_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        # 使用创建的员工账号登陆系统进行操作
        LoginH4.login_page_h4(driver, '1111', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '商品管理', '品牌维护']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"品牌维护-明细"页面'):
        HomeH4.verify_page_opened(driver, '品牌维护-明细')
    with allure.step('新建品牌'):
        brand_id = '009'
        brand_name = u'古琦'
        BrandMaintainH4.create_brand(driver, brand_id, brand_name)
    with allure.step('查询新建品牌是否存在'):
        brand_label = u'【009】古琦'
        time.sleep(3)
        BrandMaintainH4.verify_brand(driver, brand_label)
    with allure.step('关闭页面'):
        title = "品牌维护-明细"
        HomeH4.close_page(driver, title)
    with allure.step("退出登陆"):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()
