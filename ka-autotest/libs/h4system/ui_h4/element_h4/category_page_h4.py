# coding=utf-8


class CategoryPageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # button: 新建分类结构 / 保存并新建 / 保存 / 取消
    button = "//span[text()='{}']"
    # 输入框： 代码 / 名称 / 经营品数量
    input_box = "//span[text()='{}']/parent::label/following-sibling::div//input"

