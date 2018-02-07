#!/usr/bin/python
#coding=utf-8

import pytest
import sys
test_flag = False
is_test = False



def inx(x):
    return x+1


def test_01():
    print os
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
minversion = pytest.mark.skipif(sys.version_info < (3,6),reason="python version is lower to 3.6")
@minversion
def test_05():
    print "version test2"

# #跳过一个测试类
# @pytest.mark.skipif(sys.platform == 'win32',\
#                     reason="does not run on windows")
# class TestPosixCalls(object):
#     def test_function(self):
#         print "will not be setup or run under 'win32' platform"
# ##跳过一个模块的全部测试
# pytestmark = pytest.mark.skipif(is_test=False)


