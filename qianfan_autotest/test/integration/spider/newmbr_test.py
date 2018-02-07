#coding=utf-8
from __future__ import unicode_literals
import requests
import json
import unittest


login_url = "https://auth-test.qianfan123.com//dpos-auth-web/s/test/login"

appinfo_url = "https://auth-test.qianfan123.com/dpos-auth-web/s//shop/appInfo?machineCode=1&shopId=s02c8032"

newmbr_url = "https://u01c-test.qianfan123.com:8302/mbr-web/s/dpos/web/031e3f0d-363b-4a35-9a38-fb817f09f190/member/save/new"

UA = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"

session = requests.Session()


login_header = {
            "User-Agent":UA,
            "Accept":"application/json, text/plain, */*",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
            }

login_postdata = {
            "login": "18602760000",
            "password": "123456",
            "captcha": "9590",
            "captchaId": "0efaa394-395b-4f0d-835e-f3368ca7ed66"
            }

"""调用login接口进行登陆"""
get_login_response = session.post(
                            timeout = 5,
                            url = login_url,
                            data = login_postdata,
                            headers = login_header
)
print (get_login_response._content)
print (get_login_response)

"""调用appinfo接口进入门店"""
get_appinfo_response = session.get(
                            timeout = 5,
                            url = appinfo_url
                        )


newmbr_header = {
            "User-Agent":UA,
            "Accept":"application/json;charset=utf-8",
            "Content-Type":"application/json"
             }

newmbr_postdata = {
                "mobile":"18602762007",
                "name":"新增会员1",
                "sex":"male",
                "birthday":{"year":"2016","month":"12","day":"06"},
                "address":"456",
                "shop":"s01c6906",
                "remark":"备注",
                "tags":[{"id":"83492d80-145e-4a8b-a586-83e0c682edea"}]
                }

"""调用new接口新增会员"""
get_newmbr_response = session.post(
                            timeout = 5,
                            url = newmbr_url,
                            data = json.dumps(newmbr_postdata,ensure_ascii=False).encode('utf-8'),
                            headers = newmbr_header
                            )
print (get_newmbr_response.content)
print (get_newmbr_response)


class Testcase(unittest.TestCase):
    """测试登陆是否成功"""
    def test_login(self):
        login_response = get_login_response
        self.assertEquals(login_response.status_code,200)

    def test_appinfo(self):
        appinfo_response = get_appinfo_response
        self.assertEquals(appinfo_response.status_code,200)

    """测试新建会员是否成功"""
    def test_newmbr(self):
        newmbr_response = get_newmbr_response
        self.assertEquals(newmbr_response.status_code,200)

