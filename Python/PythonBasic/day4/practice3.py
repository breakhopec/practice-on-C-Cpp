#coding=utf-8
#print magical triangle

row = int(input('input row:'))
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print('')

for i in range(row, 0,-1):
    for j in range(i - 1, 0, -1):
        print(' ', end='')
    for j in range(row + 1 - i, 0, -1):
        print('*', end='')
    print()

for i in range(1, row + 1):
    for j in range(row - i):
        print(' ', end='')
    for j in range(i * 2 - 1):
        print('*', end='')
    print()