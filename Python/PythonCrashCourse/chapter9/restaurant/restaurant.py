#coding=utf-8

class Restaurant(object):
    
    def __init__(self, restaurant_name, cuisine_type):
        self._restaurant_name = restaurant_name
        self._cuisine_type = cuisine_type
        self._number_served = 0

    def describe_restaurant(self):
        print('name of the restaurant: %s' % (self._restaurant_name))
        print('type: %s' % (self._cuisine_type))

    def open_restaurant(self):
        print('%s is open' % (self._restaurant_name))

    def read_served(self):
        print('%s has served %d consumer%s' % \
            (self._restaurant_name, self._number_served, \
            's' if self._number_served > 1 else ''))

    def set_number_served(self, number):
        self._number_served = number

    def increment_number_served(self, plus):
        self._number_served += plus


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self._flavors = ['chocolate', 'corn', 'strawberry']

    def read_flavors(self):
        print('we have flavors below:')
        for flavor in self._flavors:
            print(flavor, end=' ')
        print('')