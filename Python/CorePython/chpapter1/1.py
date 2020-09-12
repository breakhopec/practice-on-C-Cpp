import re
from sys import maxsize
from time import ctime
from random import randrange, choice

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(0x7fffffff)
    dtstr = ctime(dtint)
    print(dtstr)