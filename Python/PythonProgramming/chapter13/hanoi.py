'''
    汉诺塔
'''

step = 0
def move(num: int, start: str, mediator: str, target: str) -> None:
    if num == 1:
        global step
        step += 1
        print('step {}: move {} to {}'.format(step, start, target))
        return
    move(num - 1, start, target, mediator)  # 将 n-1 个轮子移到中间柱，此时中间柱为其目标
    move(1, start, mediator, target)    # 将剩下的一个轮子移到目标柱
    move(num - 1, mediator, start,target)   # 将 n-1 个轮子从中间柱移到目标柱

if __name__ == '__main__':
    towers = int(input('input num of towers you want to move: '))
    move(towers, 'A', 'B','C')