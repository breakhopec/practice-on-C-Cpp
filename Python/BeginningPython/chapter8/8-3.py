'''
    捕获异常
'''

def main():
    try:
        d1 = int(input())
        d2 = int(input())
        print(d1 / d2)
    except (ZeroDivisionError, TypeError, ValueError) as err:
        print('what you input is invalid')
        print(err)

    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError from None

if __name__ == '__main__':
    main()