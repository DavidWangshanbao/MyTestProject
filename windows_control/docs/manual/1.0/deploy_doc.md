[TOC]
## 一、Linux配置
### 1.安装pywinrm
pip install http://github.com/diyan/pywinrm/archive/master.zip#egg=pywinrm
### 2.yum install krb5-devel    
### 3.ansible主机hosts配置
172.17.122.44 ansible_ssh_user="wwwwww" ansible_ssh_pass="123456" ansible_ssh_port=5985 ansible_connection="winrm"  
**注意端口设置：  要注意的是 端口方面ssl即https方式的使用5986，http使用5985**
![image](http://img1.ph.126.net/EROqF0f2CA778yduPFOnOQ==/1862801395971472390.png)

## 二.window配置
### 1.安装安装Framework 4.5（最低3.0）
http://download.microsoft.com/download/B/A/4/BA4A7E71-2906-4B2D-A0E1-80CF16844F5F/dotNetFx45_Full_x86_x64.exe  
查看当前Framework 版本
$psversiontable 的 CLRVersion参数
![image](http://img2.ph.126.net/GTVmFDcY46N_aJ9P0ooA2A==/6597356739193756253.png)

### 2.修改注册表变量，设置powershell本地脚本运行权限为remotesigned
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\ScriptedDiagnostics
![image](http://img0.ph.126.net/eCezKnfHxqMzAxQNHqBb4g==/6597535959588803577.png)

### 3.升级到powershell-3.0及winrm
#### 方法一：
https://github.com/cchurch/ansible/blob/devel/examples/scripts/upgrade_to_ps3.ps1    

下脚本保存至本地后，右键选择“使用PowerShell运行”，执行完毕重启系统后，在PowerShell执行Get-Host命令结果如下图所示PowerShell版本为3.0为正常。 
#### 方法二：
下载powershell-3.0的更新补丁，此补丁同时集成WMF3.0，winrm等  
https://www.microsoft.com/en-us/download/confirmation.aspx?id=34595  
或者  
https://download.microsoft.com/download/E/7/6/E76850B8-DA6E-4FF5-8CCE-A24FC513FD16/Windows6.1-KB2506143-x64.msu  
**注意：这个更新包依赖于.net3.0以上版本，如果未安装.net，会有提示"此更新不适应于您的计算机"**  
安装完成之后需要重启，重启后检验powershell版本
![image](http://img2.ph.126.net/95daJmvTWdX3nP4mTGy-uw==/6597539258123686904.png)

### 4.配置WinRM
#### 1.winrm service 默认都是未启用的状态，先查看状态；如无返回信息，则是没有启动；
```
winrm enumerate winrm/config/listener
```
#### 2.针对winrm service 进行基础配置：
```
winrm quickconfig
``` 

#### 3.查看winrm service listener
```
winrm e winrm/config/listener
```
#### 4.为winrm service 配置auth
```
winrm set winrm/config/service/auth '@{Basic="true"}'
``` 
#### 5.为winrm service 配置加密方式为允许非加密：
```
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
```
#### 6.查看winrm是否运行
```
winrm qc
```
好了，远程Windows主机配置到此结束，我们验证配置的是否有问题。



## 3.使用Ansible控制Windows主机
区别于控制Linux主机，win主机的命令，需要加上win_,具体支持情况请见官网  
http://docs.ansible.com/ansible/list_of_windows_modules.html


1.创建文件夹
```
ansible windows -m win_file -a "path=f:\LOG state=directory"
```
![image](http://img1.ph.126.net/APcBZQJeFbeK6moj56-f6A==/1284088843774079371.png)

2.执行cmd命令重启
```
ansible windows -m win_shell -a "shutdown -r -t 1"
或者
ansible windows -m win_reboot
```
3.启动windows服务
```
ansible windows -m win_service -a "name=VMnetDHCP state=started"
```

```
参考：  
http://blog.51cto.com/mengix/1862959
https://www.cnblogs.com/kingleft/p/6391652.html
https://www.jianshu.com/p/ea9cd9ecb494
http://docs.ansible.com/ansible/latest/intro_windows.html
```
