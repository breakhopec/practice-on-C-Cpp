#coding=utf-8

import os
import time


def main():
    content = 'Github 欢迎你...                   '
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()