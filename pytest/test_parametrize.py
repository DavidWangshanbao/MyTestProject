#!/usr/bin/python
#coding=utf-8


import  pytest


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




