#coding=utf-8
import json

def main():
    text = [1, 2, 3, 2]

    with open('file/number.json', 'w') as file_objects:
        json.dump(text, file_objects)

    with open('file/number.json', 'r') as file_objects:
        list1 = list(json.load(file_objects))
        list1.append(5)
        list1.sort()

    print(list1)

if __name__ == '__main__':
    main()