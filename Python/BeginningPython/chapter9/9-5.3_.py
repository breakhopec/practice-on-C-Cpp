class A(object):

    def __init__(self, value):
        self._value = value

    def __getattr__(self):
        print('not exist')
        return None

    def __getattribute__(self):
        return super().__getattribute__()


a = A(1)
print(a.values)
print(a.a)