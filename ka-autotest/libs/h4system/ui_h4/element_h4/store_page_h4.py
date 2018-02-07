# coding=utf-8


class StorePageH4(object):
    # 新建
    button = "//span[text()='{}']"
    # iframe
    iframe = "iframe#MdataContent"
    # 门店代码 / 中文名称 / 配货价
    text_input = "//span[text()='{}']/ancestor::td//input"
    # 区域 / 配货价 /记账单位
    setting_input = "//span[text()='{}']/ancestor::td//input[@aria-readonly='false']"
    # 缴款银行信息模块， 银行信息表格中的代码一列
    bank_input = "//input[@name='daBank']"
    # 保存
    save = "//span[text()='更多']/ancestor::a/preceding-sibling::*//span[text()='保存']"
    # 缴款银行信息模块， 插入行， 删除行
    data_operate = "//span[text()='账号']/parent::div/parent::div" \
                   "/parent::div/parent::div/parent::div/parent::div/parent::*" \
                   "/parent::*/parent::*/preceding-sibling::div//span[text()='{}']"
    # 单位类型: 连网连锁店，配送中心，物流中心，分公司，连锁内加盟，连锁外加盟...
    store_type = "//span[text()='{}']/parent::*/parent::*/preceding-sibling::td/div/div"



