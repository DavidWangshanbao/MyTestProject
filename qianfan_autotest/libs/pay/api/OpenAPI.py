# coding=utf-8
from __future__ import unicode_literals, print_function
import json
import requests
# from utils import baseurl_strip
from const import *


def MD5sign(StringA):
    """
    MD5签名认证
    """
    key = "2abe125e9d208e116928cd894cfc08b7"
    StringTemp = StringA + key
    print("StringA:" + StringA)
    # print(StringTemp)

    #  md5 sign result
    # import md5 模块过期
    # m1 = md5.new()
    # m1.update(StringTemp)
    # print("md5 sign result:" + m1.hexdigest())

    #  hashlib sign result
    import hashlib
    m2 = hashlib.md5()
    m2.update(StringTemp.encode('utf-8'))
    # print("hashlib sign result:" + m2.hexdigest())

    # 返回 md5 sign result
    return m2.hexdigest()


def RSAsign(StringA):
    """
    RSA签名认证
    """
    print("StringA:" + StringA)

    #  rsa sign by crypto
    #  import rsa
    # from Crypto import Random
    from Crypto.Hash import SHA
    # from Crypto.Cipher import PKCS1_v1_5
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.PublicKey import RSA
    import base64
    # need pem files
    # rsa库签名失败
    # with open('rsa_private_key.pem', 'rb') as privatefile:
    #   keydata = privatefile.read()
    # private_key = rsa.PrivateKey.load_pkcs1(keydata)  # int() argument must be a string or a number, not 'Sequence'
    # print("keydata:" + keydata)

    # print("private_key_str:" + private_key_str)
    # private_key = rsa.PrivateKey.load_pkcs1(private_key_str) # int() argument must be a string or a number, not 'Sequence'

    # signature = rsa.sign(StringA, private_key, 'SHA-1')
    # signature_base64 = base64.b64encode(signature).decode('utf-8')
    # print("rsa sign:" + signature)
    # print("rsa sign result:" + signature_base64)

    with open('rsa_private_key.pem') as f:
        key = f.read()
        # print("key:" + key)
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(StringA.encode('utf-8'))
        sign = signer.sign(digest)
    print("rsa sign result：" + base64.b64encode(sign))
    # 返回 md5 sign result
    return base64.b64encode(sign)

''' 根据 key 生成pem file
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
#from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA as RSA_Crypto
#from base64 import b64decode
#key = base64.b64decode(key)
private_key = RSA_Crypto.importKey(key)
#print(private_key.exportKey())
privHandle = open('rsa_private_key.pem', 'wb')
privHandle.write(private_key.exportKey())
privHandle.close()
'''


def submit(bizData, signType):
    """
    提交支付下单请求
    :param session:
    :param baseurl:使用默认值
    :param bizData:string类型 json.loads 转为dict类型
    :param signType:MD5/RSA
    :return:
    """
    PREFIX = "gateway"

    url = HOST + "/" + PREFIX + "/"

    appId = "qfotjilp35r9tqb8"
    serviceName = "pay.gateway.paysubmit"

    import time
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(timestamp)

    import uuid
    nonce = uuid.uuid1()
    # print(nonce)

    # StringA = "appId=qfotjilp35r9tqb8&bizData={"payCode":"280182378340183"}&serviceName=pay.gateway.paysubmit"
    StringA = r'''appId=qfotjilp35r9tqb8&bizData={"payCode":"280182378340183"}&serviceName=pay.gateway.paysubmit'''
    print('======example =====')
    if signType == "RSA":
        assert RSAsign(StringA) == "LSgA37gt8zQor+F770GOgIG6wOo6ju2BzIiZ3ODVwkmXJ1j3S9w4Ao5AwlriQAAQoSSJ8N1Acjw4IkIkwzEMEdqvBuVIMgENBr+BnTPx//mYz1FnsYTnxBm7tp7jC6DreVLp/dCzbMlhkcX3W4ylQDrETZgy4CwwZbH9Y6gXXkw=","RSA签名失败"
    else:
        signType == "MD5"
        assert MD5sign(StringA) == "97dbd192fa66a39bb6beafb11ce5062e", "MD5签名失败"

    print('======TestCase =====')
    # print(bizData)
    # python 中不需要转义
    # bizData1 = bizData.replace('"','\\"')
    StringA = "appId=" + appId + "&bizData=" + bizData + "&charset=UTF-8&nonce=" + unicode(nonce) \
              + "&serviceName=" + serviceName + "&signType=" + signType + "&timestamp=" + timestamp + "&version=2.0"

    if signType == "RSA":
        sign = RSAsign(StringA)
    else:
        signType == "MD5"
        sign = MD5sign(StringA)

    gateway_request = {
        "appId": appId,
        "bizData": bizData,
        "charset": "UTF-8",
        "nonce": unicode(nonce),
        "serviceName": serviceName,
        "sign": sign,
        "signType": signType,
        "timestamp": timestamp,
        "version": "2.0",
    }
    # print(gateway_request)
    # print(json.dumps(gateway_request,ensure_ascii=False))
    reqBody = json.dumps(gateway_request, ensure_ascii=False).encode('utf-8')
    # print(reqBody)
    return requests.post(url, timeout=HTTP_REQUEST_TIMEOUT, data=reqBody, headers=HEADERS)
