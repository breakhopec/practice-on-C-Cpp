#coding=utf-8
import time

class date(object):
    @property
    def age(self):
        return time.localtime(time.time())[0] - self._birth

    @property
    def birth(self):
        if not (self._str.startswith('AD') or self._str.startswith('BC')):
            if self._str.startswith('-'):
                return 'BC' + self._str[1:]
            else:
                return 'AD' + self._str

        return self._str

    @birth.setter
    def birth(self, year):
        self._str = year
        if year.startswith('AD'):
            self._birth = int(year[2:])
        elif year.startswith('BC'):
            self._birth = -int(year[2:])
        else:
            self._birth = int(year)

def main():
    age = date()
    age.birth = input('input birth year:')
    print(age.birth)
    print(age.age)

if __name__ == '__main__':
    main()