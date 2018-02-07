#coding=utf-8
from __future__ import unicode_literals
import pytest
import unittest
import requests

from libs.pay.api.submit import submit

@pytest.mark.pay
class PaySubmitTest(unittest.TestCase):
    @pytest.mark.pay
    def test_case1(self):
        try:
            req = r'''
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
            res = submit(req)
            if res.status_code != 200:
                raise ValueError(res.text)
            print('======test_case1 result=====')
            # response json内容
            # json_data = res.json()
            #  print(json_data)
            # response 文本
            print(res.text)
            #self.assertEqual(len(json_data.get('data')), len(res))
        except Exception as e:
            self.fail(e.message)

    @pytest.mark.pay
    @pytest.mark.chinese
    def test_case2(self):
        try:
            req = r'''
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
            res = submit(req)
            if res.status_code != 200:
                raise ValueError(res.text)
            print('======test_case2 result=====')
            # response json内容
            # json_data = res.json()
            #  print(json_data)
            # response 文本
            print(res.text)
            #self.assertEqual(len(json_data.get('data')), len(res))
        except Exception as e:
            self.fail(e.message)
if __name__ == '__main__':
    pytest.main([__file__,'-sv'])
3