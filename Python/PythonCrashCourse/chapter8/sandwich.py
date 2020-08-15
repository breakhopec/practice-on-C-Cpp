#coding=utf-8

def description(*ingredients):
    for ingredient in ingredients:
        print(ingredient, end=' ')
    print('')

def main():
    description('beef', 'apple', 'milk')
    description('pear')
    description('pork', 'melon')

if __name__ == '__main__':
    main()