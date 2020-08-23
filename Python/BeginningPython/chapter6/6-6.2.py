'''
    练习二分查找
'''
def b_search(sequence, number, lower, upper):
    if lower == upper:
        try:
            assert number == sequence[lower]
        except AssertionError:
            print('element \'{}\' not in list'.format(number))

    else:
        mid = (lower + upper) // 2
        if number > sequence[mid]:
            b_search(sequence, number, mid + 1, upper)
        else:
            b_search(sequence, number, lower, mid)

def main():
    sequence = [1, 3, 11, 30, 45, 63, 82, 91, 100]
    sequence.sort()
    b_search(sequence, 30, 0, 8)

if __name__ == '__main__':
    main()