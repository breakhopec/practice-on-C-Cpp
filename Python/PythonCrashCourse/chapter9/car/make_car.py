#coding=utf-8
import car

def main():
    my_tesla = car.ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()

if __name__ == '__main__':
    main()