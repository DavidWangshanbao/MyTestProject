# coding=utf-8

"""
门店员工管理
"""


class StoreStaffManagementPageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # 门店
    store_id = "//span[text()='门店']/parent::*/following-sibling::*/descendant::input[@aria-readonly='false']"
    store_name = "//span[text()='门店']/parent::*/following-sibling::*/descendant::input[@aria-readonly='true']"
    # 添加 / 确认全部
    button = "//span[text()='{}']"
    # 保存成功 / 删除成功
    prompt = "//div[text()='{}']"
