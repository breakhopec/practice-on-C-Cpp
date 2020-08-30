'''
    x 皇后问题，自己的尝试！
'''

num = int(input('input the number of queens: '))
queen = [None] * num
count = 0

def set_position(x, y):
    '设置位置'
    queen[x] = y

def conflict(x, y):
    '检测是否冲突'
    flag = False
    for x_l in range(x):
        if y == queen[x_l] \
            or y == queen[x_l] + (x - x_l) \
            or y == queen[x_l] - (x - x_l):
            flag = True
    return flag

def print_res():
    '根据列表输出结果'
    print(count)
    for x in range(num):
        for i in range(num):
            if i  == queen[x]:
                print('■ ', end='')
            else:
                print('□ ', end='')
        print()
    print()

def reset():
    '输出结果后清空列表'
    queen = [None] * num
    
def place(x, checkerboard):
    '开始回溯'
    if x == num:
        global count
        count += 1
        if checkerboard == True:
            print_res()
        reset()
        return

    for y in range(num):
        if conflict(x, y) == False:
            set_position(x, y)
            place(x + 1, checkerboard)
    return

def main():
    checkerboard = input('do you want to show each checkerboard? (y/n)')
    place(0, True if checkerboard.lower() == 'y' else False)
    print('the number of result is {}'.format(count))

if __name__ == '__main__':
    main()