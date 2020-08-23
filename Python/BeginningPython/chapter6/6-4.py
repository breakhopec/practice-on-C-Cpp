def story(**kwds):
    return 'Once upon a time, there was a ' \
    '{job} called {name}.'.format_map(kwds)
def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)
def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None: # 如果没有给参数stop指定值，
        start, stop = 0, start # 就调整参数start和stop的值
    result = []
    i = start # 从start开始往上数
    while i < stop: # 数到stop位置
        result.append(i) # 将当前数的数附加到result末尾
        i += step # 增加到当前数和step（> 0）之和
    return result

print(story(job='man', name='joe'))
print(power(2, 3, 'a', 'b', 'c'))
print(interval(10, step=2))