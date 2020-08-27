'''
    从list、dict 和str 派生
'''

def check_index(index):
    if index == 0:
        raise IndexError('list index out of range')


class CounterList(list):
    '从零开始的列表'
    def __init__(self, *args):
        super().__init__(args)
        self.counter = 0

    def __getitem__(self, index):
        check_index(index)
        self.counter += 1   #列表访问次数
        return super().__getitem__(index - 1 if index > 0 else index)

l = CounterList(1, 3, 5, 7)
print(l[-3])
l[1] = 0
print(l[1])
print(l.counter)