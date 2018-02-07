# coding=utf-8
"""
供应商
[基础资料-供应商管理-供应商]
[供应商-汇总]
"""
import time

import allure
from allure.constants import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains

from libs.h4system.ui_h4.element_h4.supplier_page_h4 import SupplierPageH4


class SupplierH4(object):
    """
    新增供应商
    supplier_id:供应商代码,
    supplier_name：供应商名称,
    statement：供应商状态
    备注：如果输入中文，则需要在文本前加上字母u， 例如：u"供应商名称A"
    """

    @staticmethod
    def create_supplier(driver, supplier_id, supplier_name, statement):
        # driver = webdriver.Chrome()
        text1 = "新建"
        text2 = "代码"
        text3 = "名称"
        text4 = "业务信息"
        text5 = "供应商状态"
        text6 = "保存"
        driver.switch_to_frame(driver.find_element_by_css_selector(SupplierPageH4.iframe))
        time.sleep(1)
        driver.find_element_by_xpath(SupplierPageH4.button.format(text1)).click()
        # 填写代码，名称
        time.sleep(1)
        driver.find_element_by_xpath(SupplierPageH4.input_box.format(text2)).clear()
        driver.find_element_by_xpath(SupplierPageH4.input_box.format(text2)).send_keys(supplier_id)
        driver.find_element_by_xpath(SupplierPageH4.input_box.format(text3)).clear()
        driver.find_element_by_xpath(SupplierPageH4.input_box.format(text3)).send_keys(supplier_name)
        allure.attach("填写代码和名称", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 设置供应商状态为已合作
        driver.find_element_by_xpath(SupplierPageH4.button.format(text4)).click()
        driver.find_element_by_xpath(SupplierPageH4.input_box.format(text5)).clear()
        driver.find_element_by_xpath(SupplierPageH4.input_box.format(text5)).send_keys(statement)
        driver.find_element_by_xpath(SupplierPageH4.button.format(text4)).click()
        allure.attach("设置供应商状态", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 保存
        actions = ActionChains(driver)
        save = driver.find_element_by_xpath(SupplierPageH4.button.format(text6))
        actions.move_to_element(save).click().perform()
        allure.attach("保存新建供应商", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()
