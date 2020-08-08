#coding=utf-8

def max2(list1):
    max1rd, max2nd = (list1[0], list1[1]) \
                    if list1[0] > list1[1] \
                     else (list1[1], list1[0])

    for index in range(2, len(list1)):
        if list1[index] > max1rd:
            max2nd = max1rd
            max1rd = list1[index]

    return [max1rd, max2nd]

def main():
    list1 = [1, 5]
    print(max2(list1), end='')

if __name__ == '__main__':
    main()