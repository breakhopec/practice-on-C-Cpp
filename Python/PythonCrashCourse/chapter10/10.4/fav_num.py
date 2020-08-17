#coding=utf-8
import json

def main():
    try:
        with open('file/fav_num.json', 'r') as file_objects:
            num = json.load(file_objects)
    except FileNotFoundError:
        with open('file/fav_num.json', 'w') as file_objects:
            num = input('input your favorite number: ')
            json.dump(num, file_objects)

    else:
        print('your favorite number is %s' % (num))

if __name__ == '__main__':
    main()