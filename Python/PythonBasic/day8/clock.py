#coding=utf-8
from time import sleep
from os import system

class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def process(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def print_time(self):
        print('%02d:%02d:%02d' % \
            (self.hour, self.minute, self.second))

def main():
    t = Clock(23, 59, 58)
    while True:
        system('cls')
        t.print_time()
        t.process()
        sleep(0.999)

if __name__ == '__main__':
    main()