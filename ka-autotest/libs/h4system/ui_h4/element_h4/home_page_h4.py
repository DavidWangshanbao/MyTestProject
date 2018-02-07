# coding=utf-8


class HomePageH4(object):
    # 登录的用户
    username = 'a#username.dropdown'
    # 菜单
    menu = "//div[@class='item-triangle']/preceding-sibling::div[text()='{}']"
    # 三级菜单中的【付款方式】
    pay_way = "//div[text()='付款方式组']/parent::*/preceding-sibling::*/descendant::div[text()='付款方式']"
    # 页面选项卡title
    page_title = "//div[@class='text-overflow-ellipsis']"
    # 关闭页面选项卡按钮[X]
    close_page = "//div[text()='{}']/following-sibling::button"
    # 退出
    log_out = "a#logout"


MENU_PARENT = "//div[text()='{}']/parent::*"
MENU_FOLLOW = "/following-sibling::*/descendant::div[text()='{}']"
MENU_PRECEDE = "/preceding-sibling::*/descendant::div[text()='{}']"


"""
当重复的菜单后面存在兄弟级菜单时
title1：传入兄弟级菜单title
title2：传入重复的菜单title
"""


def location_pre(title1, title2):
    element = MENU_PARENT.format(title1) + MENU_PRECEDE.format(title2)
    return element


"""
当重复的菜单前面存在兄弟级菜单时：
title1：传入兄弟级菜单title
title2：传入重复的菜单title
"""


def location_follow(title1, title2):
    element = MENU_PARENT.format(title1) + MENU_FOLLOW.format(title2)
    return element









