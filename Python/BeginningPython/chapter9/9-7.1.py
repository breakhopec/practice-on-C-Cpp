'''
    理解生成器
'''

def flatten(nested):
    try:
        try:    #检查是否为字符串
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element

    except TypeError:
        yield nested
        
l = [1, 2, [3, 4, [5], [6, 7, [8]], 9, [10], 'abc', (1, 2)], {'a': 1, 'b': 2}]

for i in flatten(l):
    print(i, end=' ')