'''
    找出合法邮箱
'''

import re

line = r'In-Reply-To: <20041219013308.A2655@bozz.floop> Mime- version: 1.0'
c_pat = r'\<(.+)@(.+?)\>'
m = re.search(c_pat, line)
f, b = m.span(1)
# 使用两种不同方法访问
print('username:', line[f:b])
print('server:', m.group(2))