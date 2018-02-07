#!/usr/bin/python
#coding=utf-8


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

