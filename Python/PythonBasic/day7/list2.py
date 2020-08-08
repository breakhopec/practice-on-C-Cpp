#coding=utf-8
import sys

def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f)) 
    print(f)
    for var in f:
        print(var, end=' ')

if __name__ == '__main__':
    main()