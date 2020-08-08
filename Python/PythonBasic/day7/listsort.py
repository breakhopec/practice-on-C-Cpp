#coding=utf-8

def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    list4 = sorted(list1, key=len)
    list_all = [list1, list2, list3, list4]

    for index in list_all:
        print(index)

    list_all[0].sort(reverse=True)
    print(list1)
    list_all[0].sort(key=len)
    print(list1)
    list1.remove(list1[0])
    print(list1)

if __name__ == '__main__':
    main()