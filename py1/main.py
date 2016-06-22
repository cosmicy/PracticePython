#!/usr/bin/env python
# coding=utf-8

import cy.Define
import common


def func():
    print("hello")
    print(cy.Define.strName)
    print(cy.Define.nAge)
    print("pocketgit")
    common.test()
    # common.my_abs('free')
    print(common.my_abs(3.36))

    print(common.power(4, 5))

# 主函数
if __name__ == '__main__':
    func()

