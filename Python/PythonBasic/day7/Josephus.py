#coding=utf-8

def main():
    people = [True] * 31
    num = 30
    pos = 0

    for _ in range(15):
        count = 0
        while count < 9:
            pos += 1
            if pos >30:
                pos = 1
            if people[pos]:
                count += 1
        people[pos] = False

    for i in range(1, 31):
        print('Jesus' if people[i] == True else 'Other',end=' ')

if __name__ == '__main__':
    main()