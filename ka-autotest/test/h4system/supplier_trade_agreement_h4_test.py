#  coding=utf-8
import pytest
import time
from behave.model import Feature
from selenium import webdriver
import allure

from libs.h4system.ui_h4.page_h4.audit_document_h4 import AuditDocumentH4
from libs.h4system.ui_h4.page_h4.home_h4 import HomeH4
from libs.h4system.ui_h4.page_h4.login_h4 import LoginH4
from libs.h4system.ui_h4.page_h4.supplier_trade_agreement_list_h4 import SupplierTradeAgreementH4


@allure.feature("新增[供应商贸易协议调整单]单据")
@allure.story("hhh")
@allure.step("hhh")
@pytest.mark.supplier_trade_agreement_h4
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.11.104:8080/hdpos4-web')
    with allure.step('登录账户'):
        LoginH4.login_page_h4(driver, 'hdposadmin', '123456', '6284')
    with allure.step('验证是否登录成功'):
        LoginH4.verify_login_h4(driver)
    with allure.step('点击左侧菜单'):
        list1 = ['基础资料', '供应商管理', '供应商贸易协议调整单']
        HomeH4.click_menu(driver, list1)
    with allure.step('验证是否打开"供应商贸易协议调整单-汇总"页面'):
        HomeH4.verify_page_opened(driver, '供应商贸易协议调整单-汇总')
    with allure.step("新增供应商贸易协议调整单"):
        supplier_name = "0000"
        sign = u"签约人"
        SupplierTradeAgreementH4.create_supplier_trade_agreement(driver, supplier_name, sign)
    time.sleep(1)
    driver.quit()









