import fileinput
import sys

for line in fileinput.input('somefile.txt'):
    print(line, end='')
fileinput.close()

with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line, end='')