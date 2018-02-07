# coding=utf-8
from __future__ import unicode_literals
from selenium.webdriver.common.keys import Keys
from utils.commons import *


class Navigator(object):
    @classmethod
    def navigate(cls, driver, *navigations):
        """
        :param driver: Selenium driver
        :param navigations: 菜单项名,菜单级别根据参数个数浮动
        :return: 
        """
        count = 0
        for x in navigations:
            if count == 1:
                element = driver.find_element_by_xpath('//td[@class="subMenu"]//div[@class="caption"][text()="{}"]'.format(x))
                driver.execute_script("arguments[0].scrollIntoView()", element)
                element.click()
            else:
                element = driver.find_element_by_xpath('//div[@class="caption"][text()="{}"]'.format(x))
            # while not element.is_displayed():
                # Navigator().downScroll(driver)
                # wait_for(1)
                # if element.is_displayed(): break
                # Navigator().upScroll(driver)
                # wait_for(1)
                # break
                driver.execute_script("arguments[0].scrollIntoView()", element)
                if not Navigator().is_expanded(driver, x): element.click()
                wait_for(1)
            count += 1

    def is_expanded(self, driver, menu_item):
        """ 判定菜单是否展开
        :param driver: Selenium driver
        :param menu_item: 菜单项名
        :return:
        """
        elem = driver.find_element_by_xpath(
            "//div[text()='{}']/parent::*/preceding-sibling::td[contains(@class, 'dotCell')]".format(menu_item))
        attr = elem.get_attribute('outerHTML')
        if attr.find('dot-expanding') != -1:
            return True
        return False

    def upScroll(self, driver):
        """
        往上滚动查找隐藏的目录
        :param driver: Selenium driver
        :return: 
        """
        upScroll = driver.find_element_by_css_selector('.rbm-ScrollPanel .rb-UScrollButton .arrow')

        while upScroll.is_displayed():
            upScroll.click()

    def downScroll(self, driver):
        """
        往下滚动查找隐藏的目录
        :param driver: 
        :return: 
        """
        downScroll = driver.find_element_by_css_selector('.rbm-ScrollPanel .rb-DScrollButton .arrow')

        while downScroll.is_displayed():
            downScroll.click()
