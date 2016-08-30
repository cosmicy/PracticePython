#py文件,建立后即可高亮
import os
from os.path import join,getsize

print("hello")

dirs=os.listdir()
print(dirs)

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

for dir in dirs:
    if(os.path.isdir(dir)):
        print(getdirsize(dir))
    else:
        print(getsize(dir))