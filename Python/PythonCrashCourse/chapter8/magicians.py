#coding=utf-8

def show_magicians(name_list):
    for name in name_list:
        print(name, end=' ')
    print('')

def make_great(name_list):
    for index in range(len(name_list)):
        name_list[index] = 'the Great ' + name_list[index]

def main():
    magicians = ['A', 'B', 'C', 'D', 'E']
    show_magicians(magicians)
    make_great(magicians)
    show_magicians(magicians)

if __name__ == '__main__':
    main()