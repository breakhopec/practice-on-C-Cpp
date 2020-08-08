#coding=utf-8
#find perfect number in 1000
from math import sqrt

for i in range(1, 1001):
    mid = int(i/2)
    sum = 0
    for j in range(1, mid+2):
        if i%j == 0:
            sum += j

    if sum == i:
        print(i, end=' ')