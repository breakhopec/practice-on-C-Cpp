#coding=utf-8

def add(a=0, b=1, c=2):
    return a + b + c

def caculate(string, *args):
    res = 0
    if string == 'add':
        for i in args:
            res += i

    elif string == 'minus':
        for i in args:
            res -= i

    else:
        return 'invalid operator'

    return res

print(add(), end=' ')
print(add(b=2), end=' ')
operate = input('the operation:')
print(caculate(operate, 1, 2), end='')