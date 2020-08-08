#coding=utf-8

items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)

scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
print(scores.get('狄仁杰', 20))
print(scores)