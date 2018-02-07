## 默认测试点
1. 默认执行当前目录下的所有以test_为前缀(test_\*.py)或以_test为后缀(\*_test.py)的 文件
2. 以Test为前缀的类，Test_Class()
3. 以test_为前缀的函数，test_one()




## 安装
pip install -U pytest  
pytest --version

## 测试CASE
#### 1.函数测试
```
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    
```    
#### 2.类测试
```
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert 'e' in x
```

#### 2.测试异常
```
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```


#### 3.fixture()
被@pytest.fixture()修饰的函数，其他函数在作为参数调用时，都会先测试这个函数
有三种调用方式如下
```
@pytest.fixture()
def before():
    print ("\nthis is call before")
    

def test_01(before):
    print ("this is test01")

@pytest.mark.usefixtures("before")
def test_02():
    print ("this is test01")
    
@pytest.mark.usefixtures("before")
class TestClass():
    def test_one(self):
        print ("this is test03")
        assert inx(4) == 3

    def test_two(self):
        print ("this is test04")
        assert  inx(4) == 5
```

```
@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
        yield smtp #相当于根据范围进行return,
        #在测试完成后返回（根据范围而定，比如此处就是测试完整个module返回smtp）
        
```

fixture的params参数，会有一个固定的request参数，指向被修饰的函数本身
```
@pytest.fixture(params=[1,2,3])
def test_data(request):
    return request.param

def test_01(test_data):
    print ("data is {}".format(test_data))
    assert test_data != 2
```

fixture的autos参数实现自动调用，
一般和scope参数结合使用，scope有四个值  
session：每个session只运行一次（暂时不清楚session的含义）  
module：每个module的所有test只运行一次  
class：每个class的所有test只运行一次,class外的test函数都运行  
function：每个test函数都运行，默认是function的scope
```
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('-----------------')

@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('-----------------')

def test_one():
    print('in test_one()')

def test_two():
    print('in test_two()')
```
比如你的所有test都需要连接同一个数据库，那可以设置为module，只需要连接一次数据库，对于module内的所有test，这样可以极大的提高运行效率。


## 命令行参数使用
### 1.返回码
```
Exit code 0:	All tests were collected and passed successfully
Exit code 1:	Tests were collected and run but some of the tests failed
Exit code 2:	Test execution was interrupted by the user
Exit code 3:	Internal error happened while executing tests
Exit code 4:	pytest command line usage error
Exit code 5:	No tests were collected
```

### 测试指定项
####  1.测试整个module
pytest test_mod.py
####  2.测试整个文件夹
pytest testing/
####  3.通过关键字测试（比较少用）
pytest -k "MyClass and not method"  
可以使用表达式，比如就是测试TestMyClass.test_something
而不会测试TestMyClass.test_method_simple
####  4.节点测试（::操作符）
##### 1.测试指定文件的某个测试  
```
pytest test_mod.py::test_func
```
##### 2.测试指定文件指定测试类的测试
```
pytest test_mod.py::TestClass::test_method
```
##### 3.测试已经标记过的测试
```
def func(x):
    return x + 1

@pytest.mark.My_test 
def test_answer():
    assert func(3) == 5
```
```
pytest -m My_test
```

##### 4.定义失败几次停止测试
```
pytest -x            # stop after first failure
pytest --maxfail=2    # stop after two failures
```
##### 5.在代码内直接调用pytest
```
def func(x):
    return x + 1

@pytest.mark.My_test 
def test_answer():
    assert func(3) == 5
    
    
if __name__ == "__main__":
    pytest.main()
    #pytest.main(['-m', 'My_test'])
    #pytest.main(['-m My_test'])
```
##### 6. pytest -h/--help获取更多参数介绍


## Pytest进阶
### 1. 一般断言
```
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    
#可以加说明
def test_answer():
    assert inx(4) == 6,u"与实际情况不符"
```

### 2. 异常断言测试
```
# 针对异常进行测试
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    with pytest.raises(ZeroDivisionError) as excinfo:
        def f():
            return  1/0
        f()
    print excinfo.type,excinfo.value
    
# 使用pytest.mark.xfail()
def f():
    return  1/0
    
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    f()

```

#### 自定义异常信息
```
#使用message参数
def test_f():
    with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        pass
```

####  匹配异常信息
```
def test_f():
    with pytest.raises(ValueError, match=r'must be \d+$'):
        raise ValueError("value must be 42")
```



#### 直接在raises方法内测试异常
```
def f(x):
    return 1/x

def test_f():
    #pytest.raises(ZeroDivisionError, lambda: 1/1)
    #pytest.raises(ZeroDivisionError,f,0)
    #pytest.raises(ZeroDivisionError,f,x=0)
    pytest.raises(ZeroDivisionError,"f(0)")
```


### 3. 警告断言测试
和异常测试类似，简单描述下
```
import warnings
import pytest

def api_v1():
    warnings.warn("api v1, should use functions from v2",UserWarning)
    return 1

def test_one():
    assert api_v1() == 1


def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)


def test_warning2():
    with pytest.warns(UserWarning, match=r'must be \d+$'):
        warnings.warn("value must be 42", UserWarning)

# 也可以直接使用以下直接测试
# pytest.warns(expected_warning, func, *args, **kwargs)
# pytest.warns(expected_warning, "func(*args, **kwargs)")
def f(x):
    warnings.warn("value must be {}".format(x), UserWarning)


def test_f():
    #pytest.warns(UserWarning,f,20)
    #pytest.warns(UserWarning, f, x= 20)
    pytest.warns(UserWarning,"f(20)")
```


### 4. Skip,skipif的使用
使用Skip,skipif跳过测试项
```
import pytest
import sys


test_flag = False
is_test = False

def inx(x):
    return x+1

def test_01():
    assert inx(4) == 5


@pytest.mark.skip(reason="no way of currently testing this")
def test_02():
    assert inx(4) == 6


def test_03():
    if not is_test:
        pytest.skip("don't need to test it")
    assert inx(4) == 5

##跳过模块的所有测试项，2.9版本支持
# if not test_flag:
#     pytest.skip("skipping all tests", allow_module_level=True)



@pytest.mark.skipif(sys.version_info < (3,6),reason="python version is lower to 3.6")
def test_04():
    print "version test"

#给skipif赋值，起个别名
minversion = @pytest.mark.skipif(sys.version_info < (3,6),reason="python version is lower to 3.6")
@minversion
def test_05():
    print "version test2"
    
    
# 可以从其他模块导入这个skipif名称
# test_myothermodule.py
from test_mymodule import minversion

@minversion
def test_anotherfunction():
    pass
    
```
```
#跳过一个测试类
@pytest.mark.skipif(sys.platform == 'win32',
                    reason="does not run on windows")
class TestPosixCalls(object):
    def test_function(self):
        print "will not be setup or run under 'win32' platform"
```
```
#跳过一个模块内的所有测试
# 定义一个名称为pytestmark的全局变量
pytestmark = pytest.mark.skipif(test_condition = False)
```

```
# 如果一个模块导入失败，跳过测试
ifexist_aabbcc = pytest.importorskip("aabbcc")
#ifexist_pytest = pytest.importorskip("pytest", minversion="1.3")
```

### 5. xfail的使用
使用xfail来期望某测试项失败
```
import  pytest

fail_flag = False

#直接标记
@pytest.mark.xfail
#如果意外测试通过，判定为xpassed,失败则是xfailed
def test_01():
    assert 1

##代码内xfail
def test_02():
    assert 1
    if fail_flag:
        pytest.xfail("customer fail")##无条件的判定为xfailed

#strict 使xpass标记为failed
@pytest.mark.xfail(strict = True)
def test_03():
    assert 1

#增加条件及原因
@pytest.mark.xfail(fail_flag,reason ="my define failed")
def test_04():
    assert 1

#不执行
@pytest.mark.xfail(run = False)
def test_05():
    assert 1
```




### 6. @pytest.mark.parametrize标记的使用
```
import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 110),
])
def test_01(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6*9",110,marks=pytest.mark.skip),##或者pytest.mark.xfail
])
def test_02(test_input,expected):
    assert eval(test_input) == expected


#多个parmetrize可使多个参数相互组合
@pytest.mark.parametrize("x",[0,1])
@pytest.mark.parametrize("y",[2,3])
def test_03(x, y):
    assert  x * y  ##0*2 0*3 1*2 1*3
```

参考官方文档：
https://docs.pytest.org/en/latest/contents.html

有什么问题大家可以相互交流
