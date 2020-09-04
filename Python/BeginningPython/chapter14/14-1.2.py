'''
    找 url
'''
from urllib.request import urlopen
import fileinput
import re

webpage = urlopen('https://baidu.com')
pat = re.compile(r'url=(.+?)"')
for line in webpage.readlines():
    m = re.search(pat, str(line, encoding='utf-8'))
    if m:
        print(m.group(1))

webpage = url