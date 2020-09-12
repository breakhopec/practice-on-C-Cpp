import re

def sub_fun(match):
    if match.group(1) == 'I':
        return r'<br>{}</br>'.format(match.group(1))
    else:
        return r'<b>{}</b>'.format(match.group(1))

pat = re.compile(r'(www\.)?[a-zA-Z0-9]+(?=.com)')
m = re.search(pat, 'www.google.com.hk')
print(m.span())
pat = re.compile(r'\w+@(?!<=www\.)(\w+\.)*(com|co\.\w{2})')
m = re.match(pat, 'breakhopec@google.com.hk')
print(m.group())
pat = re.compile(r'\bthe\b')
m = re.search(pat, 'the')
print(m.group())
pat = re.compile(r'[\w]{3}-[\d]{3}')
m = re.findall(pat, 'abc-123 cde-456 grh-351')
print(m)
str1 = '**I** say **hello world**'
pat = re.compile(r'\*\*(.+?)\*\*')
m = re.sub(pat, sub_fun, str1)
print(m)
pat = re.compile(r'(?:(x)|y)(?(1)y|x)')
print(re.search(pat, 'xy').group(1))