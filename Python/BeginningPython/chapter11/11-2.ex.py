f = open('somefile.txt', 'rt')
print(f.readline())
print(f.readlines())
f.close()
f = open('somefile.txt', 'at')
writetext = ['msg1\n', 'msg2\n']
f.writelines(writetext)
f.close()