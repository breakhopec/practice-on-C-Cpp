#coding=utf-8
#find prime in 100

for num in range(2, 101):
    end = int(num ** 0.5 + 1)
    is_prime = True

    for x in range(2, end):
        if num % x == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=' ')