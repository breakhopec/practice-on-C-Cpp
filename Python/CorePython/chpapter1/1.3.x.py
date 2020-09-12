import re
filename = 'data.dat'

with open(filename, 'r') as file_object:
    data = file_object.read()

pattern = re.compile(r'''
    ([a-z]+)
    \s+
    ([0-9a-z/]+)
    \s+
    ([A-Z][a-z]{2}\ \d{2}\ \d{2}\:\d{2})
    (\s+\((.+)\))?
    ''', re.VERBOSE)

for item in pattern.findall(data):
    print(item)

with open(filename, 'r') as file_object:
    for each_line in file_object.readlines():
        print(re.split(r'\t+', each_line.strip()))