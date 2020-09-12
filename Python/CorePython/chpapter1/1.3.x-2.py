import re
filename = 'tasklist.txt'

with open(filename, 'r') as file_object:
    data = file_object.read()

pattern = re.compile(r'''
    ([\w\.]+(?:\ [\w.]+)*)
    \s\s+
    (\d+)
    \ 
    ([A-Z][a-z]+)
    \s\s+
    (\d+)
    \s\s+
    ([\d,]+)\ K
    ''', re.VERBOSE)

print(pattern.findall(data))