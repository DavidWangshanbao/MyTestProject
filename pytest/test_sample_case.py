#!/usr/bin/python
#coding=utf-8

import pytest

def inx(x):
    return x+1

def test_answer():
    assert inx(4) == 6,u"与实际情况不符"



# @pytest.fixture()
# def before():
#     print ("\nthis is call before")
#
#
# def test_01(before):
#     print ("this is test01")
#
# @pytest.mark.usefixtures("before")
# def test_02():
#     print ("this is test01")
#
# @pytest.mark.usefixtures("before")
# class TestClass():
#     def test_one(self):
#         print ("this is test03")
#         assert inx(4) == 3
#
#     def test_two(self):
#         print ("this is test04")
#         assert  inx(4) == 5
# fixture参数
# @pytest.fixture(params=[1,2,3])
# def test_data(request):
#     return request.param
#
# def test_01(test_data):
#     print ("data is {}".format(test_data))
#     assert test_data != 2

#c测试异常
# def f():
#     raise ValueError(1)
#
# def test_mytest():
#     with pytest.raises(ValueError):
#         f()

# @pytest.fixture(scope="module", autouse=True)
# def mod_header(request):
#     print('\n-----------------')
#     print('module      : %s' % request.module.__name__)
#     print('-----------------')
#
#
# @pytest.fixture(scope="function", autouse=True)
# def func_header(request):
#     print('\n-----------------')
#     print('function    : %s' % request.function.__name__)
#     print('-----------------')

# @pytest.mark.My_test
# def test_one():
#     print('in test_one()')
#
# def test_two():
#     print('in test_two()')





