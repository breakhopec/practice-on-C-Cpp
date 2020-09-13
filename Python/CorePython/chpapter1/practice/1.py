import re

pattern = re.compile(r'[bh][aiu]t')
strs = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']

for s in strs:
    print(pattern.match(s))