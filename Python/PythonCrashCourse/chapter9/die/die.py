#coding=utf-8
import random

class Die(object):

    def __init__(self, sides=6):
        self._sides = sides

    def roll_die(self, times=1):
        for time in range(times):
            print(random.randint(1, self._sides), end=' ')
        print('')