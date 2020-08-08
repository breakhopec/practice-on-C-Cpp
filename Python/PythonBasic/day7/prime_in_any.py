#coding=utf-8
import sys
import math

def main():
    ran = int(input('please input range:'))
    list1 = [x for x in range(ran + 1)]
    print(f'size of list:{sys.getsizeof(list1)}')
    end = int(math.sqrt(ran))
    
    for var in range(2, end + 1):
        i = 2
        if list1[var] != 0:
            while var * i <= ran:
                list1[var * i] = 0
                i += 1
    
    count = 0
    for i in range(2, ran + 1):
        if list1[i] != 0:
            #print(list1[i], end=' ')
            count += 1
    
    print(f'the num of prime:{count}', end='')

if __name__ == '__main__':
    main()