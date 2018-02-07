# coding=utf-8
from __future__ import unicode_literals
import pytest
import unittest
import requests

from libs.pay.api.OpenAPI import submit


@pytest.mark.pay
class PaySubmitTest(unittest.TestCase):

    @pytest.mark.pay
    @pytest.mark.OpenAPI
    def test_case1(self):

        bizData = '''
            {
                "amount": 0.01,
                "storeNo": "0088",
                "tenantId": "testbn01",
                "uuid": "20171205-19064711",
                "orderNumber": "20171205-19064711",
                "payCode": "1810086129382927472",
                "products": [{
                    "amount": 10.99,
                    "productBrand": null,
                    "productCode": "6944094959141",
                    "productName": "pen",
                    "productSort": null,
                    "quantity": 1.01
                },
                    {
                        "amount": 9.99,
                        "productBrand": null,
                        "productCode": "6944094959100",
                        "productName": "game",
                        "productSort": null,
                        "quantity": 9.99
                    }]
            }'''
        resMD5 = submit(bizData, "MD5")

        if resMD5.status_code != 200:
            raise ValueError(resMD5.text)
        print('======pay result=====')
        # response json内容
        # json_data = res.json()
        #  print(json_data)
        # response 文本
        print(resMD5.text)

        resRSA = submit(bizData, "RSA")
        if resRSA.status_code != 200:
            raise ValueError(resRSA.text)
        print(resRSA.text)


    @pytest.mark.pay
    @pytest.mark.OpenAPI
    @pytest.mark.Chinese
    def test_case2(self):

        bizData = '''
            {
                "amount": 0.01,
                "storeNo": "0088",
                "tenantId": "testbn01",
                "uuid": "20171205-19064711",
                "orderNumber": "20171205-19064711",
                "payCode": "1810086129382927472",
                "products": [{
                    "amount": 10.99,
                    "productBrand": null,
                    "productCode": "6944094959141",
                    "productName": "pen",
                    "productSort": null,
                    "quantity": 1.01
                },
                    {
                        "amount": 9.99,
                        "productBrand": null,
                        "productCode": "6944094959100",
                        "productName": "game中文",
                        "productSort": null,
                        "quantity": 9.99
                    }]
            }'''
        resMD5 = submit(bizData, "MD5")

        if resMD5.status_code != 200:
            raise ValueError(resMD5.text)
        print('======pay result=====')
        # response json内容
        # json_data = res.json()
        #  print(json_data)
        # response 文本
        print(resMD5.text)

        resRSA = submit(bizData, "RSA")
        if resRSA.status_code != 200:
            raise ValueError(resRSA.text)
        print(resRSA.text)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
3
