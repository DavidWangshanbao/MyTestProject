# coding=utf-8
"""
功能授权
[系统管理-用户权限-功能授权]
[功能授权]
"""
import time

import allure
from allure.constants import AttachmentType
from selenium.webdriver import ActionChains
from libs.h4system.ui_h4.element_h4.function_authorization_page_h4 import FunctionAuthorizationPageH4


class FunctionAuthorizationH4(object):
    """
    新增岗位
    group：所属组织,
    code：代码,
    name：名称
    """

    @staticmethod
    def create_post(driver, group, code, name):
        text1 = "新岗位"
        text2 = "代码"
        text3 = "名称"
        text4 = "确定"
        driver.switch_to_frame(driver.find_element_by_css_selector(FunctionAuthorizationPageH4.iframe))
        time.sleep(1)
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text1)).click()
        # 设置组织，代码，名称
        group_element = driver.find_element_by_xpath(FunctionAuthorizationPageH4.group).is_displayed()
        if group_element == 0:
            time.sleep(2)
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.group).clear()
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.group).click()
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.group).send_keys(group)
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.text_input.format(text2)).click()
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.text_input.format(text2)).clear()
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.text_input.format(text2)).send_keys(code)
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.text_input.format(text3)).click()
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.text_input.format(text3)).clear()
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.text_input.format(text3)).send_keys(name)
        allure.attach("填写岗位信息：组织，代码，名称", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text4)).click()
        allure.attach("完成岗位创建", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()

    """
    设置岗位权限
    post_name:填写岗位的代码和名称,例如“11[店长]”，其中11为岗位代码，店长为岗位名称，[]符号不能省略
    """

    @staticmethod
    def post_authorization(driver, post_name):
        text1 = "功能权限"
        text2 = "模块"
        text3 = "全部模块保存为读写"
        actions = ActionChains(driver)
        driver.switch_to_frame(driver.find_element_by_css_selector(FunctionAuthorizationPageH4.iframe))
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(post_name)).click()
        # 点击[功能权限]
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text1)).click()
        # 勾选全部模块
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.check_box.format(text2)).click()
        allure.attach("勾选全部模块", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 右键点击模块
        element1 = driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text2))
        actions.context_click(element1).perform()
        # 点击全部模块保存为读写
        element3 = driver.find_elements_by_xpath(FunctionAuthorizationPageH4.button.format(text3))
        for i in range(len(element3)):
            element4 = element3[i].is_displayed()
            if element4:
                element3[i].click()
                break
        driver.switch_to_default_content()

    """
    设置岗位成员
    post_name:岗位名称
    """

    @staticmethod
    def post_member(driver, post_name):
        driver.switch_to_frame(driver.find_element_by_css_selector(FunctionAuthorizationPageH4.iframe))
        time.sleep(1)
        # 切换到岗位成员模块
        text1 = "岗位成员"
        text2 = "添加"
        text3 = "确认全部"
        actions = ActionChains(driver)
        # 选择要设置权限的岗位
        driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(post_name)).click()
        post = driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text1))
        actions.move_to_element(post).click().perform()
        allure.attach("切换到[岗位成员]", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        add = driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text2))
        actions.move_to_element(add).click().perform()
        allure.attach("弹出对话框", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        confirm = driver.find_element_by_xpath(FunctionAuthorizationPageH4.button.format(text3))
        actions.move_to_element(confirm).click().perform()
        allure.attach("确认添加全部成员", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 点击保存
        time.sleep(1)
        save_element = driver.find_element_by_xpath(FunctionAuthorizationPageH4.save_2)
        actions.move_to_element(save_element).perform()
        save_element.click()
        driver.switch_to_default_content()
