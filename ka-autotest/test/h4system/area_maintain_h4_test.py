# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.area_maintain_h4 import AreaMaintainH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4


@pytest.mark.area_maintain_h4
def test():
    """
    地区维护
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '门店管理', '门店资料', '地区维护']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"地区维护-明细"页面'):
        HomeH4.verify_page_opened(driver, '地区维护-明细')
    with allure.step("新增地区"):
        code = '06'
        name = u'北京3'
        AreaMaintainH4.add_new_area(driver, code, name)
    with allure.step("退出登陆"):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()
