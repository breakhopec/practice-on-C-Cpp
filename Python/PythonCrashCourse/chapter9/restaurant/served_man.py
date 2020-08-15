#coding=utf-8
from restaurant import Restaurant

restaurant = Restaurant('TRUMP', 114514)
restaurant.read_served()
restaurant.set_number_served(1)
restaurant.read_served()
restaurant.increment_number_served(5)
restaurant.read_served()