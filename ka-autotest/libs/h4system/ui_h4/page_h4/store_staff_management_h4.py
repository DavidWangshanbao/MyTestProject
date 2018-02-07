# coding=utf-8
"""
门店员工管理
[基础资料-员工管理-门店员工管理]
[门店员工管理-明细]
"""
import time

import allure
from allure.constants import AttachmentType

from libs.h4system.ui_h4.element_h4.store_staff_management_page_h4 import StoreStaffManagementPageH4


class StoreStaffManagementH4(object):
    """
    添加员工到门店
    store_id: 门店代码
    """

    @staticmethod
    def staff_related_store(driver, store_id):
        text1 = "添加"
        text2 = "确认全部"
        driver.switch_to_frame(driver.find_element_by_css_selector(StoreStaffManagementPageH4.iframe))
        time.sleep(1)
        # 设置门店
        driver.find_element_by_xpath(StoreStaffManagementPageH4.store_id).click()
        driver.find_element_by_xpath(StoreStaffManagementPageH4.store_id).clear()
        driver.find_element_by_xpath(StoreStaffManagementPageH4.store_id).send_keys(store_id)
        driver.find_element_by_xpath(StoreStaffManagementPageH4.store_name).click()
        allure.attach("设置要添加员工的门店", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 确认添加全部
        driver.find_element_by_xpath(StoreStaffManagementPageH4.button.format(text1)).click()
        driver.find_element_by_xpath(StoreStaffManagementPageH4.button.format(text2)).click()
        time.sleep(1)
        allure.attach("确认添加全部", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()
