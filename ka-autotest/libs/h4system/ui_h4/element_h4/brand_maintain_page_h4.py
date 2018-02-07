# coding=utf-8
"""
品牌维护
[基础资料-商品管理-品牌维护]
[品牌维护-明细]
"""


class BrandMaintainPageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # 新品牌
    button = "//span[text()='{}']"
    # 品牌维护-新品牌：代码 / 名称
    brand_id = "//span[text()='{}']/parent::label/following-sibling::*//input[@aria-readonly='false']"
    # 保存 / 保存
    text_button = "//span[text()='保存并新建']/ancestor::a/following-sibling::a//span[text()='{}']"
    # 品牌,填写的内容格式为【brand_id】brand_name,例如:'【11】11',可用于验证新增品牌是否成功
    brand_text = "//label[text()='{}']"
    # 菜单中的所有品牌
    brand_all = "div.x-tree-view.hb-tree.x-fit-item.x-tree-view-default>div.x-grid-item-container>table"
    # 定位菜单中的某一个品牌，填写数字，一般定位最后一个品牌即是新创建的品牌
    brand_one = "//table[@data-recordindex='{}']"
    # 获取某一个品牌的信息
    brand_infor = "//table[@data-recordindex='{}']//span[@class='x-tree-node-text ']"

