'''
Python yield 使用浅析
https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
'''
def feb(maxf):
    '''feb'''
    fen, feba, febb = 0, 0, 1
    while fen < maxf:
        yield febb
        feba, febb = febb, feba + febb
        fen = fen + 1

for i in feb(10):
    print(i)
