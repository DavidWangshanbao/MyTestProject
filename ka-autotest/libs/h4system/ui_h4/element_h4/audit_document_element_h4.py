# coding=utf-8


class AuditDocumentElementH4(object):
    # 下拉按钮
    drop_down = "//span[text()='保存']/ancestor::span/following-sibling::span[@class='x-btn-arrow-el']"
    # 下拉菜单中的选项
    drop_menu = "a.x-menu-item-link"
    # iframe
    iframe = "iframe#MdataContent"
    # 保存为已预审， 保存为已审核， 保存为已发货...
    drop_content = "//span[text()='{}']"
    # 单据头文本
    title_text = "//span[text()='保存']/ancestor::a/parent::div/" \
                 "label[contains(@class, 'fa-file-text')]/following-sibling::label"
