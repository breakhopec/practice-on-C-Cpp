#coding=utf-8
import die

def main():
    die1 = die.Die()
    die2 = die.Die(10)
    die3 = die.Die(20)
    die1.roll_die()
    die2.roll_die(10)
    die3.roll_die(10)

if __name__ == '__main__':
    main()