# coding=utf-8
import time
from libs.h4system.ui_h4.element_h4.employee_page_h4 import EmployeePageH4


class EmployeeH4(object):
    """
    员工
    [基础资料-员工管理-员工]
    [员工-汇总]
    code: 代码
    name：名称 输入中文时，前面要添加字母u
    password: 密码
    confirm_password：确认密码
    """

    @staticmethod
    def create_employee(driver, code, name, password, confirm_password):
        driver.switch_to_frame(driver.find_element_by_css_selector(EmployeePageH4.iframe))
        time.sleep(2)
        text1 = '新建'
        text2 = "代码"
        text3 = "中文姓名"
        text4 = "是否系统用户"
        text5 = "密码"
        text6 = "确认密码"
        text7 = "保存"
        driver.find_element_by_xpath(EmployeePageH4.button.format(text1)).click()
        time.sleep(1)
        # 填写代码，中文名称，勾选是否系统用户
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text2)).send_keys(code)
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text3)).send_keys(name)
        driver.find_element_by_xpath(EmployeePageH4.check_box.format(text4)).click()
        elements = driver.find_elements_by_xpath(EmployeePageH4.button.format(text5))
        if len(elements) < 0:
            time.sleep(1)
        # 设置密码，确认密码
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text5)).click()
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text5)).clear()
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text5)).send_keys(password)
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text6)).click()
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text6)).clear()
        driver.find_element_by_xpath(EmployeePageH4.text_input.format(text6)).send_keys(confirm_password)
        # 点击保存
        driver.find_element_by_xpath(EmployeePageH4.button.format(text7)).click()
        driver.switch_to_default_content()
