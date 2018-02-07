# coding=utf-8


class EmployeePageH4(object):
    # 新建 / 保存
    button = "//span[text()='{}']"
    # iframe
    iframe = "iframe#MdataContent"
    # 输入框： 代码 / 中文姓名 / 密码 / 确认密码 / 助记码
    text_input = "//span[text()='{}']/ancestor::td//input"
    # 是否系统用户够选框
    check_box = "//label[text()='是否系统用户']/preceding-sibling::span"
