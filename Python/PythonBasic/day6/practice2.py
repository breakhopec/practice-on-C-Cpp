#coding=utf-8

def is_palindrome(num):
    tmp1 = num
    tmp = 0
    while num > 0:
        tmp = tmp * 10 + num % 10
        num //= 10

    return True if tmp1 == tmp else False

print('not a palindrome' \
    if is_palindrome(int(input('input a number:'))) == False \
    else 'palindrome',end='')