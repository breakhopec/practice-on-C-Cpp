#coding=utf-8
#fibonacci

a = 0
b = 1
for i in range(20):
    print(b, end=' ')
    c = a + b
    a = b
    b = c