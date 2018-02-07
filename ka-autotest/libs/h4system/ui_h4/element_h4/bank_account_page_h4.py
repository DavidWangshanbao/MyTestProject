# coding=utf-8


class BankAccountPageH4(object):
    # 此处填写按钮的文本即可，例如：保存并新建 / 保存 / 取消 / 功能 / 批量添加
    button = "//span[text()='{}']"
    # 代码 / 英文名称 / 中文名称 / 财务代码 / 银行账号 / 用途
    input = "//span[text()='{}']/parent::*/following-sibling::*/descendant::*/input"
    # iframe
    iframe = "iframe#MdataContent"
    # 表格文本
    text_content = "//td/div[text()='{}']"
    # 银行档案用途输入框文本框
    application = "//span[text()='银行档案用途']/parent::*/following-sibling::*/descendant::input"
    # 银行档案用途输入框文本
    application_value = "//span[text()='银行档案用途']/parent::*/following-sibling::*" \
                        "/descendant::input[@value='门店缴款']"
    # 确认全部
    select_all = "//span[text()='确认全部']"
    # 员工代码
    employee_code = "//div[text()='{}']"


"""
点击【银行账户档案维护-明细】页面右上角的【功能】按钮，显示下拉菜单，元素定位：
tabindex = -1， 银行用途与员工关系
tabindex = 0， 查找定位
"""
function_pre = "//a[@tabindex='{}']"
function_behind = "/span[text()='{}']"


def bank_account_function(index, title):
    element_location = function_pre.format(index) + function_behind.format(title)
    return element_location






