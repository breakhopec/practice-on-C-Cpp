#coding=utf-8
import random

def generate_code():
    all_ch = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = int(input('number :'))
    s = ''
    end = len(all_ch)-1

    for i in range(num):
        s += all_ch[random.randint(0, end)]

    print(s, end='')

def main():
    generate_code()

if __name__ == '__main__':
    main()