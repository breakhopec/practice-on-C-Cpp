#coding=utf-8

class slot(object):
    __slots__ = ('_name', '_age', '_score')

    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score

    @property
    def info(self):
        return [self._name, self._age, self._score]

    @info.setter
    def info(self, value):
        if value[0] == 'name':
            self._name = value[1]
        elif value[0] == 'age':
            self._age = value[1]
        elif value[0] == 'score':
            self._score = value[1]

def main():
    st = slot('dl', 18 ,660)
    print('%s %d %d' % (st.info[0], st.info[1], st.info[2]))
    st.info = ('name', 'c')
    print('%s %d %d' % (st.info[0], st.info[1], st.info[2]))
    st._name = 'dl'
    print('%s %d %d' % (st.info[0], st.info[1], st.info[2]))
    #error
    #st._gender = 'M'

if __name__ == '__main__':
    main()