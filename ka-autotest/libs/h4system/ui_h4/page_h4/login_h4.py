#  coding=utf-8
import time
import allure
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.h4system.ui_h4.element_h4.home_page_h4 import HomePageH4
from libs.h4system.ui_h4.element_h4.login_page_h4 import LoginPageH4


class LoginH4(object):

    # 登录页面功能
    @classmethod
    @allure.feature("登录账户")
    def login_page_h4(cls, driver, username, password, verify_code):
        # 输入用户名，密码，验证码
        user = driver.find_element_by_css_selector(LoginPageH4.username) \
            .is_displayed()
        if user == 0:
            WebDriverWait(driver, 10) \
                .until(expected_conditions
                       .visibility_of_element_located((By.CSS_SELECTOR, LoginPageH4.username)))
        time.sleep(1)
        driver.find_element_by_css_selector(LoginPageH4.username).send_keys(username)
        driver.find_element_by_css_selector(LoginPageH4.password).send_keys(password)
        driver.find_element_by_css_selector(LoginPageH4.verify_code).send_keys(verify_code)
        allure.attach("填写用户名，密码及验证码后", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 点击登录按钮
        driver.find_element_by_css_selector(LoginPageH4.login_button)\
            .click()

    # 验证是否登录成功
    @classmethod
    def verify_login_h4(cls, driver):
        WebDriverWait(driver, 20)\
            .until(expected_conditions
                   .visibility_of_element_located((By.CSS_SELECTOR, HomePageH4.username)))
        allure.attach("登录后", driver.get_screenshot_as_png(), type=AttachmentType.PNG)

