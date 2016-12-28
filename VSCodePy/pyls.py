# coding=utf-8

'''
列出目录下所有文件夹和文件的列表，所占大小
py文件,建立后即可高亮
F5开始调试
'''


import os
from os.path import join, getsize


def getdirsize(dirfile):
    '''doc'''
    size = 0
    for root, dirs, files in os.walk(dirfile):
        size += sum([getsize(join(root, name)) for name in files])
    return size

print("hello")

DIRS = os.listdir(".")
print(DIRS)

for d in DIRS:
    if os.path.isdir(d):
        print(d + "\t\t" + str(getdirsize(d)))
    else:
        print(d + "\t\t" + str(getsize(d)))
