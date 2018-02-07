#  千帆自动化测试用例
### Startup  
#### 1. 安装Python 库  
```
pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt  
```
#### 2. folder structue   
```
- libs 
    |
    |- dbo
         |- ui
         |- api
    |- dmm
         |- ui
         |- api
- test 
    |
    |- dbo
    |- dmm
- utils
```
#### 3. 分支策略
一般分为master和develop两个稳定分支。master分支是脚本的稳定版本，一般可用于持续集成。
develop分支是脚本的开发分支。刚开发的不稳定脚本可以在这里进行调试和优化。如果有比较大的feature变动，
也可单独拉出一个git分支进行开发，等完成再合并到develop分支。


#### 推进建议   
- 优先自动化和UI用例有关的API  
- 优先自动化本系统的功能，延迟有对外部调用功能的依赖   
- 对API的自动化测试，逐步加入的持续集成中  

#### API封装    
##### lion  
Swagger： https://auth-test.qianfan123.com/dpos-auth-web/docs/index.html     
package： libs.lion.api  

##### alps   
Swagger:  http://172.17.11.142:8000/pod-web/docs/index.html  
package:  libs.alps.api.web  

##### dbo   
Swagger: 
-    dbo-web: https://dbo-test.qianfan123.com:8307/dbo-web/s/swagger-ui.html   
-    dbo-rs: http://dbo-test.qianfan123.com:8006/dbo-rs/apidocs/swagger   

package: libs.dbo.api

##### dmm   
Swagger:    https://dmm-test.qianfan123.com:8311/dmm-web/docs/index.html   
package: libs.dmm.api  

##### spider    
Swagger:   https://u01c-test.qianfan123.com:8302/mbr-web/docs/index.html   
package: libs.mbr.api  

##### dcmdb  
Swagger: http://auth-test.qianfan123.com:8005/cmdb-rs/api-docs/index.html  
package: libs.dcmdb.api  

##### peacock    
Swagger: https://t01c-test.qianfan123.com:8301/mp-web/docs/index.html    
package: libs.mp.api  

##### dpm   
Swagger: https://dpm-test.qianfan123.com:8313/dpm-web/api-docs/index.html   
package: libs.dpm.api

##### did  
Swagger: http://did-test.qianfan123.com:8010/did-web/docs/index.html   
package: libs.did.api  

##### swan  
Swagger: https://swan-test.qianfan123.com/showwin-web-test/docs/index.html    
package: libs.swan.api

##### butterfly  
Swagger:  https://v01c-test.qianfan123.com:8303/coupon-web/api-docs/index.html    
package: libs.butterfly.api

##### pig  
Swagger: https://w01c-test.qianfan123.com:8304/prepay-web/api-docs/index.html  
package: libs.pig.api  

##### koala     
Swagger: http://z01c-test.qianfan123.com:8001/payman-web/api-docs/index.html   
package: libs.koala.api   

#### 环境的配置信息  
- libs/config.yaml  


#### [WIKI](http://github.app.hd123.cn:10080/qianfanops/qianfan_autotest/wikis/home)    

