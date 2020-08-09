#coding=utf-8
from math import sqrt

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def distance(self, x1, y1):
        t1 = (self.x - x1) ** 2
        t2 = (self.y - y1) ** 2
        return sqrt(t1 + t2)

    def position(self):
        print(f'({self.x}, {self.y})')

def main():
    point1 = Point(2, 3)
    point1.position()
    print(point1.distance(-2, 0))
    point1.move_to(0, 0)
    point1.position()
    print(point1.distance(8, 6))

if __name__ == '__main__':
    main()