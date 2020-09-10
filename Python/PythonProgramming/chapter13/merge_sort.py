'''
    归并排序
'''

def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    l1, l2 = split_list(lst)
    return merge(merge_sort(l1), merge_sort(l2))

def merge(l1: list, l2: list) -> list:
    merged = []
    p1, p2 = 0, 0
    try:
        while True:
            if l1[p1] < l2[p2]:
                merged.append(l1[p1])
                p1 += 1
            else:
                merged.append(l2[p2])
                p2 += 1
    except IndexError:      # 其中一个列表遍历完
        merged += l1[p1:] if len(l2) == p2 else l2[p2:]

    return merged

def split_list(large_list: list) -> tuple:
    mp = len(large_list) // 2
    return (large_list[:mp], large_list[mp:])

def main() -> None:
    print(merge_sort([3, 7, 2, 6, 5, 345, 657, 42, 3425, 765, 67,\
        532, 32654, 335, 3, 6, 345, 842, 93, 928]))

if __name__ == '__main__':
    main()