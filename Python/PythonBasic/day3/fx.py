#coding=utf-8
"""
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
x = int(input('input x:'))

if x > 1:
    f = 3 * x - 5
elif -1 <= x <= 1:
    f = x + 2
else:
    f = 5 * x + 3

print('f(x)=%d' % (f))