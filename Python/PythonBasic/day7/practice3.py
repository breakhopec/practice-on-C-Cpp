#coding=utf-8

def file_suffix(filename):
    dot_pos = filename.rfind('.')
    if dot_pos != -1:
        print(filename[dot_pos + 1:], end='')
    else:
        print('No suffix', end='')

def main():
    file_suffix('geosite.dat')

if __name__ == '__main__':
    main()