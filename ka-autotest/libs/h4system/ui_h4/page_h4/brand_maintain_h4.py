# coding=utf-8
"""
品牌维护
[基础资料-商品管理-品牌维护]
[品牌维护-明细]
"""
import time

import allure
from allure.constants import AttachmentType

from libs.h4system.ui_h4.element_h4.brand_maintain_page_h4 import BrandMaintainPageH4


class BrandMaintainH4(object):
    @staticmethod
    def create_brand(driver, brand_id, brand_name):
        text1 = "新品牌"
        text2 = "代码"
        text3 = "名称"
        text4 = "保存"
        driver.switch_to_frame(driver.find_element_by_css_selector(BrandMaintainPageH4.iframe))
        time.sleep(1)
        # 点击[新品牌]
        driver.find_element_by_xpath(BrandMaintainPageH4.button.format(text1)).click()
        allure.attach("显示[品牌维护-新品牌]对话框", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 输入品牌代码，名称
        driver.find_element_by_xpath(BrandMaintainPageH4.brand_id.format(text2)).clear()
        driver.find_element_by_xpath(BrandMaintainPageH4.brand_id.format(text2)).send_keys(brand_id)
        driver.find_element_by_xpath(BrandMaintainPageH4.brand_id.format(text3)).clear()
        driver.find_element_by_xpath(BrandMaintainPageH4.brand_id.format(text3)).send_keys(brand_name)
        allure.attach("输入品牌代码，名称", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 保存
        driver.find_element_by_xpath(BrandMaintainPageH4.text_button.format(text4)).click()
        driver.switch_to_default_content()

    """
    验证某品牌是否存在
    brand_label: 品牌标签，格式为【brand_id】brand_name，例如【001】德芙
    """

    @staticmethod
    def verify_brand(driver, brand_label):
        driver.switch_to_frame(driver.find_element_by_css_selector(BrandMaintainPageH4.iframe))
        time.sleep(1)
        brand_all = driver.find_elements_by_css_selector(BrandMaintainPageH4.brand_all)
        all_number = len(brand_all)
        for i in range(all_number):
            str1 = driver.find_element_by_xpath(BrandMaintainPageH4.brand_infor.format(i)).text
            if str1 == brand_label:
                str2 = "存在品牌：" + brand_label
                allure.attach(str2, driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                break
        driver.switch_to_default_content()
