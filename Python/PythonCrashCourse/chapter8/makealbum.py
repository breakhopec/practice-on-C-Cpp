#coding=utf-8

def make_album(artist, album, total_track=0):
    album = {
        'artist': artist,
        'album': album,
        'total_track': total_track
    }
    return album

def main():
    info1 = make_album('Minase Inori', 'Unknown')
    info2 = make_album('Suzuki Minori', 'Yozora', 6)
    print(info1)
    print(info2)

if __name__ == '__main__':
    main()