# coding=utf-8
"""
分类体系设定
[基础资料-类别管理-分类体系设定]
[分类体系设定]
"""
import time

import allure
from allure.constants import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains

from libs.h4system.ui_h4.element_h4.category_page_h4 import CategoryPageH4


class CategoryH4(object):

    """
    分类级别
    category_id:类别代码,
    category_name：类别名称,
    product_amount：经营品数量
    备注：
        ① 如果给一个级别创建子级别，则子级别的代码必须以父级别的代码开头，如：父级别代码：01，则子级别为：01XX
        ② 类别名称为中文时，必须加字母u，例如：u"测试级别"
    """
    @staticmethod
    def create_category(driver, category_id, category_name, product_amount):
        #driver = webdriver.Chrome()
        driver.switch_to_frame(driver.find_element_by_css_selector(CategoryPageH4.iframe))
        time.sleep(1)
        text1 = "新建分类结构"
        text2 = "代码"
        text3 = "名称"
        text4 = "经营品数量"
        text5 = "保存"
        actions = ActionChains(driver)
        driver.find_element_by_xpath(CategoryPageH4.button.format(text1)).click()
        # 设置代码， 名称， 经营品数量
        driver.find_element_by_xpath(CategoryPageH4.input_box.format(text2)).clear()
        driver.find_element_by_xpath(CategoryPageH4.input_box.format(text2)).send_keys(category_id)
        driver.find_element_by_xpath(CategoryPageH4.input_box.format(text3)).clear()
        driver.find_element_by_xpath(CategoryPageH4.input_box.format(text3)).send_keys(category_name)
        driver.find_element_by_xpath(CategoryPageH4.input_box.format(text4)).clear()
        driver.find_element_by_xpath(CategoryPageH4.input_box.format(text4)).send_keys(product_amount)
        allure.attach("填写代码，名称，经营品数量", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 保存
        save = driver.find_element_by_xpath(CategoryPageH4.button.format(text5))
        actions.move_to_element(save).click().perform()
        allure.attach("保存新增类别", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()
