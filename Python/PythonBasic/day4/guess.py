#coding=utf-8

import random

answer = random.randint(1, 100)
times = 0

while True:
    your = int(input('input number:'))
    times += 1
    if your > answer:
        print('smaller')
    elif your < answer:
        print('bigger')
    else:
        print('right')
        break

print('total times:%d' % (times))