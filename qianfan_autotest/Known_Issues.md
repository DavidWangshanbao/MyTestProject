#  已知问题
### requests相关  
#### 1. 请求body中有中文时，server端接收不完整
鼎付通用例中碰到，请求body中不带中文可以调用成功；请求带有中文时server端返回400，无效json格式     
查看ELK日志，发现server端收到的请求不完整，与请求header中的Content-Length有关，升级requests库未解决     
将请求内容保存到json文件后，再读取发送，调用成功   
修改post请求写法，json.dumps后.encode('utf-8'),也能调用成功  
```
return session.post(url, timeout=5, data=json.dumps(json.loads(query_cond, encoding='utf-8'),ensure_ascii=False).encode('utf-8'),headers=headers)
```
参考 http://www.pulpcode.cn/2015/12/09/python-requests-post-unicode-lose-data/
#### 2. 欢迎补充 
#### [WIKI](http://github.app.hd123.cn:10080/qianfanops/qianfan_autotest/wikis/home)    
