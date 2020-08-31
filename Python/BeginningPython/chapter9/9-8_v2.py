'''
    x 皇后问题，参考答案（太强了orz）
'''

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX - state[i]) in (0, nextY - i):
            return True
    return False

def queens(num, state=()):
    if len(state) == num - 1:
        for i in range(num):
            if conflict(state, i) == False:
                yield (i,)

    for nextX in range(num):
        if conflict(state, nextX) == False:
            for res in queens(num, state + (nextX,)):
                yield res + (nextX,)

def main():
    num = int(input('input the number of queens: '))
    for i in queens(num):
        print(i)

if __name__ == '__main__':
    main()