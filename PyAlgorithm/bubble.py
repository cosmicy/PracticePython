# coding=utf-8

def bubble(list):
    """bubble sort"""
    for i in range(len(list)):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

if __name__ == '__main__':
    LIST_NUM = [2, 3, 5, 7, 8, 9, 6, 54, 1, 42]
    bubble(LIST_NUM)
    print(LIST_NUM)
