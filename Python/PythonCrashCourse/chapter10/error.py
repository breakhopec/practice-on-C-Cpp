#coding=utf-8

try:
    print(3/0)
except ZeroDivisionError:
    print('you cant division by zero')