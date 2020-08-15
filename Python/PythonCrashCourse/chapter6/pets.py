#coding=utf-8

def main():
    pets = {
        'pet1': {
            'category': 'cat',
            'master': 'master1'
        },

        'pet2': {
            'category': 'dog',
            'master': 'master2'
        },

        'pet3': {
            'category': 'rabbit',
            'master': 'master3'
        }
    }

    for petname, petinfo in pets.items():
        print('%s is a %s, whose master is %s' % \
            (petname.title(), petinfo['category'], petinfo['master']))
            
if __name__ == '__main__':
    main()