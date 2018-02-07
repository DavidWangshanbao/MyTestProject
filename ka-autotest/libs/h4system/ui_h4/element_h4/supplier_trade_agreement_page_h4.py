# coding=utf-8

"""
供应商贸易协议调整单
"""


class SupplierTradeAgreementPageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # 新建 / 继续 / 取消 / 批量选择商品 / 确认全部
    button = "//span[text()='{}']"
    # 供应商
    supplier = "//span[text()='供应商']/parent::label/following-sibling::div//input[@aria-readonly='false']"
    # 对方签约人
    input_text = "//span[text()='对方签约人']/parent::label/following-sibling::div//input"
    # 确定
    confirm = "//label[text()='批量添加商品已完成！']/parent::div/parent::div/parent::div/following-sibling::" \
              "div//span[text()='确定']"
    # 下拉按钮
    drop_down = "//span[text()='保存']/ancestor::span/following-sibling::span[@class='x-btn-arrow-el']"
    # 下拉菜单中的选项
    drop_menu = "a.x-menu-item-link"
