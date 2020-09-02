'''
    模板
'''

import re

def replace(match):
    cmd = match.group(1)
    try:
        return str(eval(cmd, va_scope))
    except SyntaxError:
        exec(cmd, va_scope)
        return ''

va_scope = {}
raw1 = r'The sum of 7 and 9 is [7 + 9].'
raw2 = r'[name="Mr. Gumby"]Hello, [name]'
pat = r'\[(.+?)\]'
raw_all = raw1 + '\n' + raw2
print(re.sub(pat, replace, raw_all))