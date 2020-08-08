#coding=utf-8

a = int(input('a='))
b = int(input('b='))

print(type(a), a)
print(type(b), b)

print('%d+%d=%d'%(a, b, a + b))
print('%d-%d=%d'%(a, b, a - b))
print('%d*%d=%d'%(a, b, a * b))
print('%d+%d=%f'%(a, b, a / b))
print('%d%%%d=%d'%(a, b, a % b))
print('%d**%d=%d'%(a, b, a ** b))