#coding=utf-8

def main():

    file_path = 'text_file/pi_million_digits.txt'
    with open(file_path) as file_objects:
        lines = file_objects.readlines()

    pi_str = ''
    for line in lines:
        pi_str += line.strip()

    print(pi_str[:52], end='')

if __name__ == '__main__':
    main()