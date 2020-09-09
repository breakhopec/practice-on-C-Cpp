from random import randint

def main() -> None:
    beginner = 'B'
    count = 0
    times = int(input('imput the times you want to play: '))
    for i in range(times):
        winner = startgame(beginner)
        if winner == 'A':
            count += 1
        beginner = 'B' if beginner == 'A' else 'A'

    print('A: {:.4f}  B: {:.4f}'.format(count / times, 1 - count / times))

def startgame(beginner: str) -> str:
    scoreA, scoreB = 0, 0
    while scoreA != 15 and scoreB != 15:
        per_winner = play(beginner)
        if per_winner == 'A':
            scoreA += 1
        elif per_winner == 'B':
            scoreB += 1
        beginner = 'B' if beginner == 'A' else 'A'

    return 'A' if scoreA == 15 else 'B'

def play(beginner: str) -> str:
    if is_win(beginner):
        return beginner
    else:
        return ''

def is_win(beginner: str) -> bool:
    if beginner == 'A':
        if randint(1, 100) < 50:  # A 单局胜率为 51%
            return False
        else:
            return True
    if beginner == 'B':
        if randint(1, 100) < 50:  # B 单局胜率为 49%
            return True
        else:
            return False

if __name__ == '__main__':
    main()