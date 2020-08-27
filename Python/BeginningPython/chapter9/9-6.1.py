'''
    理解迭代器与可迭代对象
'''

class Fibs_base(object):
    
    def __init__(self, _max):
        self._p = 0
        self._c = 1
        self._max = _max

    def __next__(self):
        self._p, self._c = self._c, self._p + self._c
        if self._max == 0 or self._p < self._max:
            return self._p
        else:
            raise StopIteration()

class Fibs(Fibs_base):

    '参数为最大值范围'
    def __init__(self, max=0):
        super().__init__(max)

    def __iter__(self):
        return self

fibs = Fibs(10)
l = list(fibs)
print(l)

for i in Fibs(50):
    print(i, end=' ')
print()

for i in Fibs():
    if i > 1000:
        print(i, end=' ')
        break