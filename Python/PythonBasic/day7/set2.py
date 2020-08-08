#coding=utf-8

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)

set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set4 = {3, 4, 5}
print(set3 >= set4)
print(set3 <= set4)

set5 = {1, 2, 3}
set6 = {1, 2, 3}
print(set5 == set6)
print(set5 > set6)
print(set5 >= set6)