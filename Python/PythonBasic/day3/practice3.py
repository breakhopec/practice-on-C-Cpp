#coding=utf-8
#s of triangle

s1 = float(input('side1:'))
s2 = float(input('side2:'))
s3 = float(input('side3:'))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    p = (s1 + s2 + s3) / 2
    s = (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5
    print('s of triangle is:%.2f' % (s))
else:
    print('Please input proper side')