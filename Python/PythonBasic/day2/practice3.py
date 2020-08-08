#coding=utf-8
#check if leap year

year = int(input('year:'))

res = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(res)