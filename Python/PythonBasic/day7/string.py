#coding=utf-8

str1 = 'hello, world!'

print(str1.title())
print(str1.lower())
print(str1.upper())
print(str1.startswith('he'))
print(str1.endswith('@'))
print(str1.find('or'))
print('llo' in str1)

a, b = 2, 3
print(f'{a}*{b}={a*b}')
print('{0}*{1}={2}'.format(a, b, a*b))