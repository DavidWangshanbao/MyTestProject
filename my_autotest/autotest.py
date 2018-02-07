#!/usr/bin/python
#coding=utf-8


from selenium import webdriver


def test():
    url = "http://www.baidu.com"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_css_selector('input#kw').send_keys(u'六安瓜片')
    driver.find_element_by_css_selector("input#su").click()
    driver.quit()


test()









