#coding=utf-8

def main():
    guest = ['lp', 'lj', 'bg', 'sj']
    removed_one = 'lp'
    guest.remove(removed_one)
    print('%s canceled due to ...' % removed_one.title())
    print(guest)
    print('now I find bigger table')
    guest.insert(0, 'lzx')
    guest.insert(int(len(guest) / 2 - 1), 'djt')
    guest.append('xbz')
    print(guest)
    print('I can invite only two, now it\'s lottery time!')
    for _ in range(len(guest) - 2):
        removed_one = guest.pop()
        print('sorry %s Xp' % removed_one)
        
    del guest[0]
    del guest[0]
    print(guest)

if __name__ == '__main__':
    main()