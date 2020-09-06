from random import randint, sample, randrange

def select() -> list:
    select_ball = []
    red_ball = range(1, 34)
    select_ball = sample(red_ball, 6)
    select_ball.sort()
    select_ball.append(randint(1, 16))
    return select_ball

def print_ball(balls: list) -> None:
    for index, value in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('{:02}'.format(value), end=' ')
    print()

def main():
    t = int(input('input how many times you want: '))
    for i in range(t):
        print_ball(select())

if __name__ == '__main__':
    main()