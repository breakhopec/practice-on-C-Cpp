#coding=utf-8
#is prime?

num = int(input('input a number:'))
end = int(num ** 0.5 + 1)
is_prime = True

for x in range(2, end):
    if num % x == 0:
        is_prime = False
        break

print('this is %sa prime' % ('' if is_prime == True else 'not '), end='')