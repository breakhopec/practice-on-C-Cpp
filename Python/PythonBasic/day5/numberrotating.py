#coding=utf-8

ori_num = int(input('input number:'))
num = 0

while ori_num > 0:
    num=num * 10 + ori_num % 10
    ori_num //= 10

print('rotated number:%d' % (num))