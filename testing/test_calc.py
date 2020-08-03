#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/8/3 下午11:12
# 被测文件
import sys

import pytest

sys.path.append('..')
from pythoncode.calc import Calculator


@pytest.mark.add
def test_add1():
    cal = Calculator()
    assert 2 == cal.add(1, 1)


@pytest.mark.add
def test_add2():
    cal = Calculator()
    assert 3 == cal.add(2, 1)


@pytest.mark.div
def test_div1():
    cal = Calculator()
    assert cal.div(2, 1) == 2
