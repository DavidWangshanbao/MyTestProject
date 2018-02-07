# coding=utf-8

"""
功能授权
"""


class FunctionAuthorizationPageH4(object):
    # 新岗位
    button = "//span[text()='{}']"
    # 所属组织输入框
    # group = "//div[text()='该输入项为必输项']/preceding-sibling::*//input"
    group = "//span[text()='所属组织']/parent::label/following-sibling::div//input[@aria-readonly='false']"
    # 代码 / 名称
    text_input = "//span[text()='{}']/ancestor::label/following-sibling::*//input"
    # iframe
    iframe = "iframe#AdminContent"
    # 勾选框：模块
    check_box = "//span[text()='{}']/parent::div//div[@role='button']"
    # 功能权限模块的[保存]
    save_1 = "//span[text()='模块']/ancestor::div/preceding-sibling::*//span[text()='保存']/ancestor::a"
    # 岗位成员模块的[保存]
    save_2 = "//span[text()='添加']/ancestor::a/following-sibling::*//span[text()='保存']"
    # 保存成功
    success = "//div[text()='{}']"
