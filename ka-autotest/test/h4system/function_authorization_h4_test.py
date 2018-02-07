# coding=utf-8
import allure
import pytest
import time
from selenium import webdriver

from libs.h4system.ui_h4.page_h4.function_authorization_h4 import FunctionAuthorizationH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4


@pytest.mark.function_anthorization_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.12.23:8580/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['系统管理', '用户权限', '功能授权']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"功能授权"页面'):
        HomeH4.verify_page_opened(driver, '功能授权')
    with allure.step('新增岗位'):
        group = "0001"
        code = "20"
        name = u"烘焙师20"
        FunctionAuthorizationH4.create_post(driver, group, code, name)
        time.sleep(1)
    with allure.step("给岗位添加权限"):
        post_name = "20[烘焙师20]"
        FunctionAuthorizationH4.post_authorization(driver, post_name)
    with allure.step("关闭功能授权"):
        title = "功能授权"
        HomeH4.close_page(driver, title)
    with allure.step('点击左侧菜单'):
        list1 = ['系统管理', '用户权限', '功能授权']
        HomeH4.click_menu(driver, list1)
    with allure.step("设置岗位成员"):
        post_name = '20[烘焙师20]'
        FunctionAuthorizationH4.post_member(driver, post_name)
    with allure.step("退出登陆"):
        HomeH4.log_out(driver)
    time.sleep(1)
    driver.quit()

