#!/usr/bin/env python
# coding=utf-8


def compare(a,b):
    return a < b

    # 原来的cmp，使用functools.cmp_to_key 即可。


def test():
    print(compare(3, 7))


def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

