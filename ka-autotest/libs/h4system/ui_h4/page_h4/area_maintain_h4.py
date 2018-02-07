# coding=utf-8
"""
地区维护
基础资料-门店管理-地区维护
[地区维护-明细]页面
"""
import allure
import time
from allure.constants import AttachmentType
from libs.h4system.ui_h4.element_h4.area_maintain_page_h4 import AreaMaintainPageH4


class AreaMaintainH4(object):

    """
    添加【新地区】
    code : 设置地区代码， 如：01
    name :设置地区名称， 如：上海
    """
    @staticmethod
    def add_new_area(driver, code, name):
        new_area = "新地区"
        save = "保存"
        time.sleep(1)
        driver.switch_to_frame(driver.find_element_by_css_selector(AreaMaintainPageH4.iframe))
        driver.find_element_by_xpath(AreaMaintainPageH4.button.format(new_area)).click()
        driver.find_element_by_xpath(AreaMaintainPageH4.code_input).clear()
        driver.find_element_by_xpath(AreaMaintainPageH4.code_input).send_keys(code)
        driver.find_element_by_xpath(AreaMaintainPageH4.name_input).clear()
        driver.find_element_by_xpath(AreaMaintainPageH4.name_input).send_keys(name)
        allure.attach("填写地区代码和名称", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.find_element_by_xpath(AreaMaintainPageH4.button2.format(save)).click()
        allure.attach("添加新地区完成", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()






