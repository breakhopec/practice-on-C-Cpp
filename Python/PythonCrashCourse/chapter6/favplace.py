#coding=utf-8

def main():
    fav_places = {
        'person1': ['China', 'Hong Kong', 'Taiwan'],
        'person2': ['Japan'],
        'person3': ['US', 'Norway', 'Uk']
    }

    for person, place_info in fav_places.items():
        print('This is %s, following %s my favourite place%s:' % \
            (person.title(), 'are' if len(place_info) != 1 else 'is',\
                's' if len(place_info) != 1 else ''))
        for place in place_info:
            print(place, end=' ')
        print('\n')

if __name__ == '__main__':
    main()