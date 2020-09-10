from random import randint

def one_game() -> bool:
    initial = get_points()
    if initial == 2 or initial == 3 or initial == 12:
        return False
    elif initial == 7 or initial == 11:
        return True
    else:
        return after_once(initial)

def get_points() -> int:
    return randint(1, 6) + randint(1, 6)

def after_once(initial: int) -> bool:
    while True:
        current_point = get_points()
        if current_point == 7:
            return False
        elif current_point == initial:
            return True

def main():
    times = int(input('input how many times you want test: '))
    count = 0
    for i in range(times):
        if one_game():
            count += 1

    print('win: {:.4f}'.format(count / times))

if __name__ == '__main__':
    main()