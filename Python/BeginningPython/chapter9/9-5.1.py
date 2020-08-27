class Rectangle(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    #@property
    def _get_size(self):
        return self._width, self._height

    #@size.setter
    def _set_size(self, args_tuple):
        self._width, self._height = args_tuple

    def set_other(self, key, value):
        self.__dict__[key] = value

    size = property(_get_size, _set_size)

i = Rectangle(2, 3)
print(i.size)
i.size = 6, 7
print(i.size)
print(i.__dict__)
i.set_other('a', 1)
print(i.a)