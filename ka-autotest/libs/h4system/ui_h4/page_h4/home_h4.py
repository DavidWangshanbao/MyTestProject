#  coding=utf-8
import allure
import time
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from libs.h4system.ui_h4.element_h4.home_page_h4 import HomePageH4
from libs.h4system.ui_h4.element_h4.login_page_h4 import LoginPageH4


class HomeH4(object):
    """
    1.菜单的点击，传入列表list1，如：list1 = ['基础资料', '供应商管理', '供应商']
    2.由于二级菜单和三级菜单中都出现了【付款方式】，所以对【付款方式】采取代码中的处理方式（看代码）
    """
    @classmethod
    def click_menu(cls, driver, list1):
        time.sleep(1)
        actions = ActionChains(driver)
        for num in range(len(list1)):
            if num < (len(list1)-1):
                element = driver.find_element_by_xpath(HomePageH4.menu.format(list1[num]))
                actions.move_to_element(element).perform()
                allure.attach('鼠标移动到指定菜单栏:' + list1[num], driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            else:
                element = driver.find_element_by_xpath(HomePageH4.menu.format(list1[num]))
                actions.move_to_element(element).click()
                actions.perform()
                allure.attach("鼠标移动到指定菜单栏:"+list1[num]+" / 打开指定页面:" + list1[num],
                              driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    """
    菜单的点击
    此方法用于当出现重复的菜单title时，可选择传入的list1样式如下：
    list1 = [HomePageH4.menu.format('零售管理'),
            location_follow('零售价格', '付款方式'),
            location_pre('付款方式组', '付款方式')]
    """

    @classmethod
    def click_menu_repeat(cls, driver, list1):
        time.sleep(1)
        actions = ActionChains(driver)
        for num in range(len(list1)):
            if num < (len(list1) - 1):
                element = driver.find_element_by_xpath(list1[num])
                actions.move_to_element(element).perform()
                allure.attach('鼠标移动到指定菜单栏:' + list1[num], driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            else:
                element = driver.find_element_by_xpath(list1[num])
                actions.move_to_element(element).click()
                actions.perform()
                allure.attach("鼠标移动到指定菜单栏：" + list1[num] + " / 打开指定页面:" + list1[num],
                              driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    """
    验证页面是否正确打开
    title：页面选项卡标题，如"地区维护-明细"
    """
    @staticmethod
    def verify_page_opened(driver, title):
        allure.attach("打开页面后", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        if driver.find_element_by_xpath(HomePageH4.page_title). text != title:
            print "This is the wrong page"
        assert driver.find_element_by_xpath(HomePageH4.page_title). text == title

    """
    关闭页面选项卡
    title:页面选项卡标题，如"地区维护-明细"
    """
    @staticmethod
    def close_page(driver, title):
        actions = ActionChains(driver)
        element = driver.find_element_by_xpath(HomePageH4.close_page.format(title))
        actions.move_to_element(element).click().perform()
        time.sleep(1)
        allure.attach("关闭页面", driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    """
    退出登陆
    """
    @staticmethod
    def log_out(driver):
        actions = ActionChains(driver)
        element = driver.find_element_by_css_selector(HomePageH4.username)
        actions.move_to_element(element).perform()
        allure.attach("点击右上角的用户名", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        element2 = driver.find_element_by_css_selector(HomePageH4.log_out)
        actions.move_to_element(element2).click().perform()
        time.sleep(1)
        value = driver.find_element_by_css_selector(LoginPageH4.username).is_displayed()
        if value == 0:
            print ("退出账户异常")
        allure.attach("退出账户登陆", driver.get_screenshot_as_png(), type=AttachmentType.PNG)


































