#coding=utf-8

class Score(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

def main():
    student = Score('dl', 80)
    print(student.name)
    print(student.score)
    student.name = 'cjy'
    student.score = 90
    print(student.name)
    print(student.score)

if __name__ == '__main__':
    main()