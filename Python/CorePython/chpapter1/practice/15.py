import re

'''
    15: 4-6-5 16: 4-4-4-4
'''

pattern = re.compile(r'''
    (\d{4})\-?(\d{4})\-?(\d{4})\-?(\d{4})
    |
    (\d{4})\-?(\d{6})\-?(\d{5})''', re.VERBOSE)
print(pattern.match('1234-1234-1234-1213'))