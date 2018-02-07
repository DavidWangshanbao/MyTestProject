# coding=utf-8


class AreaMaintainPageH4(object):
    # button 新地区， 保存
    button = "//span[text()='{}']"
    # iframe
    iframe = "iframe#MdataContent"
    # 代码输入框
    code_input = "//span[text()='*']/parent::span[text()='代码']/parent::label/following-sibling::*//input"
    # 名称输入框
    name_input = "//span[text()='*']/parent::span[text()='代码']" \
                 "/ancestor::tr/following-sibling::*//span[text()='名称']" \
                 "/parent::*/following-sibling::*//input"
    # [地区维护-新地区]弹出框的按钮: 保存， 取消
    button2 = "//span[text()='保存并新建']//ancestor::a/following-sibling::*//span[text()='{}']"





