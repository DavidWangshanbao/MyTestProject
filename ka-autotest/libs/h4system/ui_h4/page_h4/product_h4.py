# coding=utf-8
import time

import allure
from allure.constants import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains

from libs.h4system.ui_h4.element_h4.product_page_h4 import ProductPageH4

"""
商品
[基础资料-商品管理-商品]
[商品-汇总]
"""


class ProductH4(object):
    """
    新增商品（统配，直配，日配，直送）
    product_id:商品id,
    product_name:商品名称,
    brand_id：品牌
    category_id：类别
    warehouse_id：仓位
    supplier_id：供应商
    ship_way：配货方式 [G货-统配 / P货-直配 / S货-直送]
    retail_price：零售价
    member_price:会员价
    high_price:最高售价
    low_price:最低售价
    trade_price:批发价
    inventory_price：库存价
    purchase_price:合同进价
    high_inventory：最高库存
    daily_product：如果要创建日配商品则设置该值为1， 非日配商品则设置为0
    备注:填写的内容为中文时，需要加字母u， 例如：u"商品名称A"
    """

    @staticmethod
    def create_product(driver, product_id, product_name, brand_id, category_id, warehouse_id,
                       supplier_id, ship_way, retail_price, member_price, high_price, low_price,
                       trade_price, inventory_price, purchase_price, high_inventory, daily_product):
        driver.switch_to_frame(driver.find_element_by_css_selector(ProductPageH4.iframe))
        time.sleep(1)
        driver.find_element_by_xpath(ProductPageH4.button.format("新建")).click()
        time.sleep(1)
        actions = ActionChains(driver)
        # 在[商品信息]模块输入[代码][名称]
        driver.find_element_by_xpath(ProductPageH4.input_box.format("代码")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("代码")).send_keys(product_id)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("名称")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("名称")).send_keys(product_name)
        allure.attach("设置商品代码和名称", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 在[出厂]模块进行设置
        driver.find_element_by_xpath(ProductPageH4.button.format("出厂")).click()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("品牌")).click()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("品牌")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("品牌")).send_keys(brand_id)
        driver.find_element_by_xpath(ProductPageH4.input_text.format("类别")).click()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("类别")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("类别")).send_keys(category_id)
        driver.find_element_by_xpath(ProductPageH4.input_text.format("仓位")).click()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("仓位")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("仓位")).send_keys(warehouse_id)
        driver.find_element_by_xpath(ProductPageH4.input_text.format("默认供应商")).click()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("默认供应商")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_text.format("默认供应商")).send_keys(supplier_id)
        driver.find_element_by_xpath(ProductPageH4.input_text.format("结算供应商")).click()
        allure.attach("在出厂模块进行设置", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 在[进销]模块输入[配货方式]
        driver.find_element_by_xpath(ProductPageH4.button.format("进销")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("配货方式")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("配货方式")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("配货方式")).send_keys(ship_way)
        allure.attach("在进销模块进行设置", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        # 在[价格]模块设置[零售价 / 会员价 / 最高售价 / 最低售价 / 批发价 / 库存价 / 合同进价 / 最高库存数]
        driver.find_element_by_xpath(ProductPageH4.button.format("价格")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("零售价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("零售价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("零售价")).send_keys(retail_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("会员价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("会员价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("会员价")).send_keys(member_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最高售价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最高售价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最高售价")).send_keys(high_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最低售价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最低售价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最低售价")).send_keys(low_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("批发价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("批发价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("批发价")).send_keys(trade_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("库存价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("库存价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("库存价")).send_keys(inventory_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("合同进价")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("合同进价")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("合同进价")).send_keys(purchase_price)
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最高库存数")).click()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最高库存数")).clear()
        driver.find_element_by_xpath(ProductPageH4.input_box.format("最高库存数")).send_keys(high_inventory)
        allure.attach("在[价格]模块进行设置", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        if daily_product == 1:
            driver.find_element_by_xpath(ProductPageH4.button.format("其他")).click()
            driver.find_element_by_xpath(ProductPageH4.input_box.format("是否日配商品")).click()
            driver.find_element_by_xpath(ProductPageH4.input_box.format("是否日配商品")).clear()
            driver.find_element_by_xpath(ProductPageH4.input_box.format("是否日配商品")).send_keys("是")
            allure.attach("在[其他]模块进行设置", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        save = driver.find_element_by_xpath(ProductPageH4.button.format("保存"))
        actions.move_to_element(save).click().perform()
        allure.attach("保存新增商品", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        driver.switch_to_default_content()


