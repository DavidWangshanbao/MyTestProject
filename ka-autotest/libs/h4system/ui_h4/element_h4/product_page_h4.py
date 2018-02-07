# coding=utf-8


class ProductPageH4(object):
    # iframe
    iframe = "iframe#MdataContent"
    # 新建
    button = "//span[text()='{}']"
    """
     [输入框]
     商品信息：代码 / 名称 / 
     进销：配货方式
     价格： 零售价 / 会员价 / 最高售价 / 最低售价 / 批发价 / 库存价 / 合同进价 / 最高库存数
     其他： 是否日配商品
    """
    input_box = "//span[text()='{}']/parent::label/following-sibling::div//input"
    """
    出厂模块：品牌 / 类别 / 仓位 / 默认供应商
    """
    input_text = "//span[text()='{}']/parent::label/following-sibling::div//input[@aria-readonly='false']"

    """
    选项配置
    [自动计算商品代码末位的条码校验 /
    自动生成拼音助记码 /
    进行代码长度限制]
    """
    configure = "//label[text()='{}']/parent::div/input"
    # 确定 / 取消
    confirm = "//div[text()='选项配置']/ancestor::div//span[text()='{}']"

