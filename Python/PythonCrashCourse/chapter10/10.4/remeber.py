#coding=utf-8
import json

def main():
    filename = 'file/username.json'
    try:
        with open(filename, 'r') as file_objects:
            name = json.load(file_objects)
    except FileNotFoundError:
        username = input('what\'s your name? ')
        with open(filename, 'w') as file_objects:
            json.dump(username, file_objects)
    else:
        print('welcom back %s' % (name))


if __name__ == '__main__':
    main()