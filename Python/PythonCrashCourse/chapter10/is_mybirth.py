#coding=utf-8

def main():

    file_path = 'text_file/pi_million_digits.txt'
    with open(file_path) as file_objects:
        lines = file_objects.readlines()

    pi_str = ''
    for line in lines:
        pi_str += line.strip()

    birth = input('enter your brithday(yy/mm/dd): ')
    pos = pi_str.find(birth)
    if pos == -1:
        print('no luck')
    else:
        print('position in pi: %d' % (pos))

if __name__ == '__main__':
    main()