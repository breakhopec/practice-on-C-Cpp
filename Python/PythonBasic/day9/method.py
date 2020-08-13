#coding=utf-8

class method(object):
    a = 0

    def foo1(self):
        print('hello')
        print(self)

    @staticmethod
    def foo2():
        print('hello')

    @classmethod
    def foo3(cls):
        print('hello')
        print(cls)

def main():
    m = method()
    print(method.a)
    print(m.a)
    method.a = 1
    print(method.a)
    print(m.a)
    m.a = 2
    print(method.a)
    print(m.a)
    method.a = 3
    print(method.a)
    print(m.a)


if __name__ == '__main__':
    main()