# coding=utf-8
"""
仓位
[基础资料-仓位管理-仓位]
[仓位-明细]
"""
import time

import allure
from allure.constants import AttachmentType
from selenium.webdriver import ActionChains

from libs.h4system.ui_h4.element_h4.warehouse_page_h4 import WarehousePageH4


class WarehouseH4(object):
    """
    创建仓位
    warehouse_id:仓位代码,
    warehouse_name：仓位名称,
    store_id：所属门店
    """

    @staticmethod
    def create_warehouse(driver, warehouse_id, warehouse_name, store_id):
        text1 = "新建"
        text2 = "代码"
        text3 = "门店"
        text4 = "全部添加"
        actions = ActionChains(driver)
        driver.switch_to_frame(driver.find_element_by_css_selector(WarehousePageH4.iframe))
        time.sleep(1)
        # 点击新建
        driver.find_element_by_xpath(WarehousePageH4.button.format(text1)).click()
        allure.attach("打开[新建仓位]", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 输入代码、 名称、门店
        driver.find_element_by_xpath(WarehousePageH4.input_box.format(text2)).clear()
        driver.find_element_by_xpath(WarehousePageH4.input_box.format(text2)).send_keys(warehouse_id)
        driver.find_element_by_xpath(WarehousePageH4.name_input).clear()
        driver.find_element_by_xpath(WarehousePageH4.name_input).send_keys(warehouse_name)
        driver.find_element_by_xpath(WarehousePageH4.input_box.format(text3)).clear()
        driver.find_element_by_xpath(WarehousePageH4.input_box.format(text3)).send_keys(store_id)
        driver.find_element_by_xpath(WarehousePageH4.store_name).click()
        allure.attach("输入仓位代码、 仓位名称、所属门店", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 添加所有的业务类型
        all_type = driver.find_element_by_xpath(WarehousePageH4.all_selection.format(text4))
        actions.move_to_element(all_type).click().perform()
        # 保存
        save_button = driver.find_element_by_xpath(WarehousePageH4.save)
        actions.move_to_element(save_button).click().perform()
        time.sleep(1)
        allure.attach("保存新仓位", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()

    """
    验证某个仓位是否存在
    warehouse_expected:传入一个列表，例如：["【0001】海鼎公司","【-】未知"]
    备注：符号【】不能省略
    此方法暂只适用于捕捉到显示的仓位及门店
    """

    @staticmethod
    def verify_warehouse(driver, warehouse_list):
        driver.switch_to_frame(driver.find_element_by_css_selector(WarehousePageH4.iframe))
        time.sleep(1)
        ware = driver.find_elements_by_xpath(WarehousePageH4.warehouse_infor)
        for i in range(len(ware)):
            print ware[i].text
            for j in range(len(warehouse_list)):
                if ware[i].text == warehouse_list[j]:
                    str1 = "存在仓位：" + warehouse_list[j]
                    allure.attach(str1, driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()
