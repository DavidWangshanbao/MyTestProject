#!/usr/bin/python
#coding=utf-8


import  pytest

fail_flag = False

@pytest.mark.xfail
#如果意外测试通过，判定为xpassed,失败则是xfailed
def test_01():
    assert 1


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

#测试代码不执行
@pytest.mark.xfail(run = False)
def test_05():
    assert 1
