#coding=utf-8

def make_user(first_name, last_name, **info):
    info_dic = {}
    info_dic['first_name'] = first_name
    info_dic['last_name'] = last_name
    info_dic['detail'] = {}
    for key, value in info.items():
        info_dic['detail'][key] = value
    return info_dic

def obtain_info(user):
    print(user['first_name'] + ' ' + user['last_name'])
    for key, value in user['detail'].items():
        print(key + ':' + value)

def main():
    user1 = make_user('Rinka', 'Kujou', \
        username='root', password='1234567890', comment='cat')
    obtain_info(user1)

if __name__ == '__main__':
    main()