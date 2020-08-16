#coding=utf-8

def main():
    
    with open('text_file/pi_digits.txt') as file1:
        #conents = file1.read()
        #
        #for char in conents:
        #    if char.isdigit() or char == '.':
        #        print(char, end='')
        lines = file1.readlines()

    print(lines)

if __name__ == '__main__':
    main()