#coding=utf-8
import creat

def make_car(manufacturer, model, **others):
    new_car = {}
    new_car['manufacturer'] = manufacturer
    new_car['model'] = model

    for key, value in others.items():
        new_car[key] = value

    return new_car

def main():
    car = make_car('subaru', 'outback', \
        color='blue', tow_package=True)
    print(car)
    p = creat.make_user('Rinka', 'Kujou', \
        username='root', password='1234567890', comment='cat')
    creat.obtain_info(p)

if __name__ == '__main__':
    main()