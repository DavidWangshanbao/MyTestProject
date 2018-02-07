# coding=utf-8
"""
仓位
"""


class WarehousePageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # 新建
    button = "//span[text()='{}']"
    # 输入框：代码 / 门店
    input_box = "//span[text()='{}']/parent::label/following-sibling::*//input[@aria-readonly='false']"
    # 门店名称输入框
    store_name = "//span[text()='门店']/parent::label/following-sibling::*//input[@aria-readonly='false']" \
                 "/parent::div/parent::div/parent::div/parent::div/following-sibling::div//input"
    # 输入框：名称
    name_input = "//span[text()='代码']/parent::label/following-sibling::" \
                 "*//input[@aria-readonly='false']/ancestor::tr//span[text()='名称']" \
                 "/parent::label/following-sibling::*//input"
    # [新建仓位]页面的[全部添加] / [仓位-明细]页面的[全部删除]
    all_selection = "//span[text()='协议']/ancestor::a/parent::div" \
                    "/parent::div/parent::div/preceding-sibling::div//span[text()='{}']"
    # [新建仓位]页面的保存按钮
    save = "//span[text()='取消']/ancestor::a/preceding-sibling::*//span[text()='保存']"
    # 左侧菜单中的仓位，填写仓位信息,例如“【0001】 海鼎公司”，仓位id和仓位name之间的空格不能省略
    warehouse_infor = "//span[@class='x-tree-node-text ']"
