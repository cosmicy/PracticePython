#!/usr/bin/env python
# coding=utf-8

import cy.Define
import common

import sys
import argparse


def func(argv):
    print("hello")
    print(cy.Define.strName)
    print(cy.Define.nAge)
    print("pocketgit")
    common.test()
    # common.my_abs('free')
    print(common.my_abs(3.36))

    print(common.power(4, 5))
    print(common.fact(5))

    p = argparse.ArgumentParser("help123")
    p.add_argument('-c', nargs='?',default='cy')
    p.add_argument('-y', nargs='?', default='wy')

    args = p.parse_args(argv[1:])
    if args.c == 'cy':
        print("-cy")

    # clean
    print("Clean my computor.")

    # Mac
    print("Mac下快速搜索或启动：Command＋Space")

    #game
    print("game save git")

# 主函数
if __name__ == '__main__':
    argv = sys.argv
    func(argv)

