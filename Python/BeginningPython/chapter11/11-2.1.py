try:
    f = open('somefile.txt', 'wt')
    f.write('this is a test msg')
    f.close()
    f = open('somefile.txt', 'rt')
    print(f.read(100))
    print(f.read())
    f.close()
except:
    f.close()