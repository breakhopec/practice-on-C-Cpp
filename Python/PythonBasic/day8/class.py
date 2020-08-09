#coding=utf-8

class indi(object):
    def __init__(self, b, c):
        self.name = b
        self.age = c
    
    def study(self, course):
        print(f'{self.name} is studying {course}')
    
    def entertainment(self, game):
        print(f'{self.name} is playing {game}')

    def p_age(self):
        print(f'{self.age}')

def main():
    he = indi('lx', 18)
    he.study('math')
    he.entertainment('ra2')
    he.p_age()

if __name__ == '__main__':
    main()
