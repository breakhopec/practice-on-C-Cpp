#coding=utf-8

def main():
    citys = {
        'city1': {
            'country': 'China',
            'population': 100
        },
        'city2': {
            'country': 'Japan',
            'population': 200
        },
        'city3': {
            'country': 'US',
            'population': 300
        }
    }

    for city in citys.keys():
        print('%s in %s has population of %d' % \
            (city.title(), citys[city]['country'], citys[city]['population']))

if __name__ == '__main__':
    main()