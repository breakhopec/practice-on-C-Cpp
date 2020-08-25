'''
    对接口的理解
'''
import abc
class Ab(abc.ABC):
    @abc.abstractmethod
    def talk(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass

class Inh(Ab):
    def talk(self):
        pass

    def write(self):
        pass

class Te(object):
    pass
i = Inh()
j = Te()
Ab.register(Te)
print(isinstance(i, Ab))
print(issubclass(Te, Ab))
#Te.talk()
#Fail: Te 有成为 Ab 的倾向，但继承失败