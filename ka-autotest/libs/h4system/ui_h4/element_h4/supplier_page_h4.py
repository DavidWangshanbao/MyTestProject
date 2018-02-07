# coding=utf-8
"""
供应商
"""


class SupplierPageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # 新建 / 业务信息
    button = "//span[text()='{}']"
    # 输入框： 代码 / 名称 / 供应商状态
    input_box = "//span[text()='{}']/parent::label/following-sibling::div//input"
