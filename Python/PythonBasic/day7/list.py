#coding=utf-8

list1 = [1, 2, 5, 10, 1000, 5000]

for element in list1:
    print(element, end=' ')

for index in range(len(list1)):
    print(list1[index],end=' ')

for index, elem in enumerate(list1):
    print(f'({index}, {elem})', end=' ')

if 2 in list1:
    list1.remove(2)

if 2 not in list1:
    list1.insert(1, 2)
print(list1)

list1.pop(-1)
print(list1)

'''def change(lst: list):
    l = lst
    l[0] = 2'''

#change(list1)
l = list1
l[0] = 2
print(list1)