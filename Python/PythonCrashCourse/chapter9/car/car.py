#coding=utf-8

class Car(object):

    def __init__(self, manufacturer, model, year):
        self._manufacturer = manufacturer
        self._model = model
        self._year = year
        self._odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self._year) + ' ' + \
            self._manufacturer + ' ' + self._model
        return long_name.title()

    def read_odometer(self):
        print('odometer: %s' % (self._odometer_reading))

    def update_odometer(self, mileage):
        self._odometer_reading = mileage

    def increment_odometer(self, mile):
        self._odometer_reading += mile


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
        

class Battery(object):

    def __init__(self, battery_size=70):
        self._battery_size = battery_size

    def describe_battery(self):
        print('this car has %d kWh battery.' % (self._battery_size))

    def get_range(self):
        print('this car can go %d miles.' % (self._battery_size * 4))

    def upgrade_battery(self):
        if self._battery_size != 85:
            self._battery_size = 85