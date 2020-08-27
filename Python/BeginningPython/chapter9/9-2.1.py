class Bird(object):
    
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('I\'m full!')

    def sing(self):
        print('Tweet!')

class SongBird(Bird):
    
    def __init__(self):
        self.sound = 'Squawk!'
        super().__init__()

    def sing(self):
        print(self.sound)

    def s1(self):
        self.sing()

    def s2(self):
        super().sing()

b1 = SongBird()
b1.s1()
b1.s2()