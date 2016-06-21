def compare(a,b):
    return cmp(a,b)


def test():
    print(compare(3,7))


def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x

