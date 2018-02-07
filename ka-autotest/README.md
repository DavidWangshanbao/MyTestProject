# KA 自动化测试用例   
### Startup  
#### 1. 安装Python 库  
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt  
```
#### 2. folder structue   
```
- libs 
    |
    |- hdcard
         |- ui
         |- api
    |- hdpos46
         |- ui
         |- api
- test 
    |
    |- integration
    |- hdcard
    |- hdpos46
- utils
```
#### 3. 分支策略  
一般分为master和develop两个稳定分支。master分支是脚本的稳定版本，一般可用于持续集成。  
develop分支是脚本的开发分支。刚开发的不稳定脚本可以在这里进行调试和优化。如果有比较大的feature变动，
也可单独拉出一个git分支进行开发，等完成再合并到develop分支。