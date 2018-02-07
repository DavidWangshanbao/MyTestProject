# coding=utf-8
"""
门店
[基础资料-门店管理-门店资料-门店]
"""
import allure
import time
from allure.constants import AttachmentType
from libs.h4system.ui_h4.element_h4.store_page_h4 import StorePageH4


class StoreH4(object):

    """
    新建门店
    store_value：门店代码
    name_value：门店名称
    area_value：区域代码
    value：只可以设置为true或者false；当为true是创建的门店为物流中心，为false时创建的为连网连锁店
    bank_value：缴款银行代码
    """
    @staticmethod
    def create_store(driver, store_value, name_value, area_value, value, bank_value):
        text1 = '新建'
        store = '门店代码'
        name = '中文名称'
        area = '区域'
        text2 = '业务信息'
        text3 = '配货价'
        text4 = '缴款银行信息'
        text5 = '插入行'
        text6 = u'自营'
        type_text1 = '连网连锁店'
        type_text2 = '配送中心'
        type_text3 = '物流中心'
        type_text4 = '分公司'
        type_text5 = '物流中心类型'
        driver.switch_to_frame(driver.find_element_by_css_selector(StorePageH4.iframe))
        time.sleep(2)
        driver.find_element_by_xpath(StorePageH4.button.format(text1)).click()
        time.sleep(1)
        # 门店代码
        driver.find_element_by_xpath(StorePageH4.text_input.format(store)).clear()
        driver.find_element_by_xpath(StorePageH4.text_input.format(store)).send_keys(store_value)
        # 中文名称
        driver.find_element_by_xpath(StorePageH4.text_input.format(name)).clear()
        driver.find_element_by_xpath(StorePageH4.text_input.format(name)).send_keys(name_value)
        # 设置区域
        try:
            driver.find_element_by_xpath(StorePageH4.setting_input.format(area)).click()
            driver.find_element_by_xpath(StorePageH4.setting_input.format(area)).clear()
            driver.find_element_by_xpath(StorePageH4.setting_input.format(area)).send_keys(area_value)
        except Exception, e:
            print "门店设置区域失败", e.message
        allure.attach("填写门店代码，门店名称，区域", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        if value:
            # 设置物流中心，取消勾选[连网连锁店]，勾选[配送中心，物流中心，分公司]
            driver.find_element_by_xpath(StorePageH4.store_type.format(type_text1)).click()
            element1 = driver.find_element_by_xpath(StorePageH4.store_type.format(type_text1)).is_selected()
            if element1:
                driver.find_element_by_xpath(StorePageH4.store_type.format(type_text1)).click()
            driver.find_element_by_xpath(StorePageH4.store_type.format(type_text2)).click()
            driver.find_element_by_xpath(StorePageH4.store_type.format(type_text3)).click()
            driver.find_element_by_xpath(StorePageH4.store_type.format(type_text4)).click()
            allure.attach("勾选单位类型", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            # 设置物流中心类型
            driver.find_element_by_xpath(StorePageH4.text_input.format(type_text5)).click()
            driver.find_element_by_xpath(StorePageH4.text_input.format(type_text5)).send_keys(text6)
            allure.attach("设置物流中心类型", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 切换到[业务信息]
        driver.find_element_by_xpath(StorePageH4.button.format(text2)).click()
        # 设置配货价为0
        driver.find_element_by_xpath(StorePageH4.setting_input.format(text3)).send_keys('0')
        allure.attach("设置配货价", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 切换到[缴款银行信息],添加缴款银行信息
        driver.find_element_by_xpath(StorePageH4.button.format(text4)).click()
        # 点击插入行，插入一条缴款银行数据
        driver.find_element_by_xpath(StorePageH4.data_operate.format(text5)).click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath(StorePageH4.bank_input).click()
            driver.find_element_by_xpath(StorePageH4.bank_input).clear()
            driver.find_element_by_xpath(StorePageH4.bank_input).send_keys(bank_value)
            allure.attach("设置缴款银行", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except Exception, e:
            print "设置缴款银行失败", e.message
        # 保存门店
        time.sleep(1)
        driver.find_element_by_xpath(StorePageH4.save).click()
        driver.switch_to_default_content()
