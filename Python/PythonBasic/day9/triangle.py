#coding=utf-8

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

def main():
    print(Triangle.is_valid(1, 2, 3))
    tr = Triangle(2, 3, 4)
    tr.is_valid(2, 3, 4)

if __name__ == '__main__':
    main()