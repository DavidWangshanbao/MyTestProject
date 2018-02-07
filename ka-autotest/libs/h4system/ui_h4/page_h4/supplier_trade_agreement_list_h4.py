# coding=utf-8
import time

import allure
from allure.constants import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains

from libs.h4system.ui_h4.element_h4.supplier_trade_agreement_page_h4 import SupplierTradeAgreementPageH4

"""
供应商贸易协议调整单
[基础资料-供应商管理-供应商贸易协议调整单]
[供应商贸易协议调整单-汇总]

"""


class SupplierTradeAgreementH4(object):

    """
    创建[供应商贸易协议调整单]单据
    supplier_name:供应商名称,
    sign：对方签约人
    备注：如果输入的文本为中文，则需加字母u，例如：u"签约人"
    """
    @staticmethod
    def create_supplier_trade_agreement(driver, supplier_name, sign):
        actions = ActionChains(driver)
        driver.switch_to_frame(driver.find_element_by_css_selector(SupplierTradeAgreementPageH4.iframe))
        time.sleep(1)
        # 点击新建，进入[供应商贸易协议调整单-明细]页面
        create = driver.find_element_by_xpath(SupplierTradeAgreementPageH4.button.format("新建"))
        actions.move_to_element(create).click().perform()
        time.sleep(1)
        # 填写供应商 / 对方签约人
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.supplier).clear()
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.supplier).send_keys(supplier_name)
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.input_text.format("对方签约人")).click()
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.input_text.format("对方签约人")).clear()
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.input_text.format("对方签约人")).send_keys(sign)
        allure.attach("设置信息：供应商，对方签约人", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.button.format("继续")).click()
        # 设置商品
        time.sleep(1)
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.button.format("批量选择商品")).click()
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.button.format("确认全部")).click()
        allure.attach("设置商品", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        time.sleep(3)
        # 点击确认，保存
        driver.find_element_by_xpath(SupplierTradeAgreementPageH4.confirm).click()
        save = driver.find_element_by_xpath(SupplierTradeAgreementPageH4.button.format("保存"))
        actions.move_to_element(save).click().perform()
        allure.attach("保存单据", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()



