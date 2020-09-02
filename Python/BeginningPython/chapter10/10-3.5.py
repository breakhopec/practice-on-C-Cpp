'''
    熟悉正则表达式基础
'''

import re

c_str = re.compile('(http(s)?://)?(www\\.)?(python)\\.com')
m = re.search(c_str, 'https://www.python.com')
print(m.group(4))

pat = '{name}'
ori = 'hello {name}'
print(re.sub(pat, 'Rinka', ori))

pat2 = r'\*([^\*]+)\*'
print(re.sub(pat2, r'<em>\1</em>', 'hello, *world*!'))

pat3 = r'\*(.+?)\*'
print(re.sub(pat3, r'<em>\1</em>', '*This* is *it*!'))

pat4 = r'\*\*(.+?)\*\*'
print(re.sub(pat4, r'<em>\1</em>', '**this** is **it**!'))