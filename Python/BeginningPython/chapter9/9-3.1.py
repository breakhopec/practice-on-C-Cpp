'''
    利用协议创建算术序列
'''

def check_index(key):
    '检查引索是否有效'
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise KeyError


class ArithmeticSequence(object):

    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)

        self.changed[key] = value

    def __delitem__(self, key):
        check_index(key)

        try:
            del self.changed[key]
        except KeyError:
            pass

s = ArithmeticSequence(1, 2)
s[4] = 1
print(s[4], s[1])
del s[4]
del s[4]
print(s[4])