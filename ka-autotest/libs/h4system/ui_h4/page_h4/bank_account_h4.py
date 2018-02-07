# coding=utf-8
import time

import allure
from allure.constants import AttachmentType
from selenium.webdriver import ActionChains
from libs.h4system.ui_h4.element_h4.bank_account_page_h4 import BankAccountPageH4, bank_account_function


"""
银行账户档案维护页面
path：财务管理》基础设置》银行账户档案维护
"""


class BankAccountH4(object):
    """
    维护银行用途与员工关系
    value:u'门店缴款' / u'供应商付款' / u'客户收款'
    """
    @staticmethod
    def relate_bank_employee(driver, value):
        bank_use = '银行档案用途'
        content = '功能'
        index = '-1'
        title = '银行用途与员工关系'
        employee_code = 'hdposadmin'
        add_text = '批量添加'
        driver.switch_to.frame(driver.find_element_by_css_selector(BankAccountPageH4.iframe))
        # 点击 功能-银行用途与员工关系
        driver.find_element_by_xpath(BankAccountPageH4.button.format(content)).click()
        driver.find_element_by_xpath(bank_account_function(index, title)).click()
        time.sleep(1)
        # 此处采用输入"u门店缴款 / u供应商付款 / u客户收款"的方式设置银行用途
        driver.find_element_by_xpath(BankAccountPageH4.application).clear()
        driver.find_element_by_xpath(BankAccountPageH4.application).send_keys(value)
        # 输入值后先点击页面的任意一点确认输入，再点击批量添加
        add = driver.find_element_by_xpath(BankAccountPageH4.button.format(add_text))
        bank = driver.find_element_by_xpath(BankAccountPageH4.button.format(bank_use))
        actions = ActionChains(driver)
        actions.move_to_element(bank).click().perform()
        actions.move_to_element(add).click().perform()
        select_all = driver.find_elements_by_xpath(BankAccountPageH4.select_all)
        if len(select_all) < 1:
            actions.move_to_element(add).click().perform()
        driver.find_element_by_xpath(BankAccountPageH4.select_all).click()
        code_list = driver.find_elements_by_xpath(BankAccountPageH4.employee_code.format(employee_code))
        if len(code_list) < 2:
            time.sleep(1)
        allure.attach("添加员工完成", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()

    """
    返回银行账户档案维护
    """
    @staticmethod
    def back_to_account(driver):
        text = '返回银行账户档案维护'
        driver.switch_to_frame(driver.find_element_by_css_selector(BankAccountPageH4.iframe))
        driver.find_element_by_xpath(BankAccountPageH4.button.format(text)).click()
        driver.switch_to_default_content()

    """
    添加银行账户档案数据，并验证数据是否创建成功
    *list1一般传入两个列表对象作为参数,这两个列表分别为输入框的名称和要输入的内容，要一一对应，例如：
    list_name = ['代码', '中文名称', '财务代码', '用途']
    list_value = ['1020', u'工商', '01', u'门店缴款']
    备注：如果输入框中填写的内容为中文，则要在中文前加字母u
    """
    @staticmethod
    def add_new_data(driver, *list1):
        argument1 = '添加'
        # rgument2：保存，取消
        argument2 = '保存'
        time.sleep(1)
        # 进入iframe内嵌框架
        driver.switch_to_frame(driver.find_element_by_css_selector(BankAccountPageH4.iframe))
        driver.find_element_by_xpath(BankAccountPageH4.button.format(argument1)).click()
        allure.attach("打开弹窗'银行账户档案维护-添加'", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        time.sleep(1)
        list_name = list1[0]
        list_value = list1[1]
        for i in range(len(list_name)):
            # 向输入框中输入内容
            driver.find_element_by_xpath(BankAccountPageH4.input.format(list_name[i])).clear()
            driver.find_element_by_xpath(BankAccountPageH4.input.format(list_name[i])).send_keys(list_value[i])
        allure.attach("填写银行账户档案维护", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.find_element_by_xpath(BankAccountPageH4.button.format(argument2)).click()
        # 退出iframe框架
        time.sleep(1)
        # 验证银行账户档案数据是否创建成功
        element = driver.find_element_by_xpath(BankAccountPageH4.text_content.format(list_value[0])).is_displayed()
        allure.attach("保存银行账户档案维护", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        if element:
            print '银行账户档案数据创建成功'
        else:
            print '银行账户档案数据创建失败'
        driver.switch_to_default_content()





