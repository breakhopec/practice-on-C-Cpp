#coding=utf-8

def main():
    
    filename = 'text_file/write_in.txt'
    with open(filename, 'w') as file_objects:
        file_objects.write('this is a test message.\n')

if __name__ == '__main__':
    main()