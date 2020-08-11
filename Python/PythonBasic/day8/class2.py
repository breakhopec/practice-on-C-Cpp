#coding=utf-8

class Class(object):
    __count = 0
    def one(self):
        self.__count = 1
        print(self.__count)

    def two(self):
        print(self.__count)

r = Class()
print(r._Class__count)
r.one()
r.two()
print(r._Class__count)