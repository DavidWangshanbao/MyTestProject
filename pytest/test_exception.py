#!/usr/bin/python
#coding=utf-8

import pytest

# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0
#
#
# def test_recursion_depth():
#     with pytest.raises(ZeroDivisionError) as excinfo:
#         def f():
#             return  1/0
#         f()
#     print excinfo.type,excinfo.value

# def test_f():
#     with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
#         pass
def f(x):
    return 1/x

def test_f():
    #pytest.raises(ZeroDivisionError, lambda: 1/1)
    #pytest.raises(ZeroDivisionError,f,0)
    #pytest.raises(ZeroDivisionError,f,x=0)
    pytest.raises(ZeroDivisionError,"f(0)")