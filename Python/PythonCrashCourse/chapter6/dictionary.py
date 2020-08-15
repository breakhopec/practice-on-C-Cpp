#coding=utf-8

def main():
    fav_lang = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'java'
    }
    ques_people = ['sarah', 'edward']

    for people in fav_lang.keys():
        if people in ques_people:
            print('Thank you %s.' % (people))
        else:
            print('I invite you to come, %s.' % (people))

if __name__ == '__main__':
    main()