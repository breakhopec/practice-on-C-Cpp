class Rectangle(object):

    def __init__(self):
        self._width = 0
        self._height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self._width, self._height = value
        elif name:
            self.__dict__[name] = value
        else:
            raise KeyError()

    def __getattr__(self, name):
        if name == 'size':
            return self._width, self._height
        else:
            return None

    def __getattribute__(self, name):
        #do something here before access value
        return super().__getattribute__(name)

a = Rectangle()
a.size = 2, 4
a.color = 'red'
print(a.size, a.color, a.__dict__)