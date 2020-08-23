'''
    递归练习与理解
    模拟阶乘
'''
import time
def pow1(base, m):  #第一种实现
    if m == 1:
        return base
    
    if int(m) & 1 == 0:
        return pow1(base * base, m / 2)
    else:
        return pow1(base * base, (m - 1) / 2) * base

def pow2(base, m):  #第二种实现，耗时
    res = 1
    for i in range(m):
        res *= base
    return res

def main():
    print('please wait about 20s')
    s1 = time.time()
    pow1(2, 1024000)
    s2 = time.time()
    pow2(2, 1024000)
    s3 = time.time()
    print('cpu time: a1: {:.4}  a2: {:.4}'.format(s2 - s1, s3 - s2))

if __name__ == '__main__':
    main()