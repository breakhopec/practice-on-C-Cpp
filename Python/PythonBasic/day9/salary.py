"""
    工资结算系统
"""

import abc
class Employee(abc.ABC):

    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def get_salary():
        pass

    def get_name(self):
        return self._name

    name = property(get_name)


class Manager(Employee):
    
    def get_salary(self):
        return 15000.0


class Programmer(Employee):

    def __init__(self, name, working_hours=0):
        super().__init__(name)
        self._working_hours = working_hours

    def set_working_hours(self, hours):
        self._working_hours = hours if hours >= 0 else 0

    def get_working_hours(self):
        return self._working_hours

    working_hours = property(get_working_hours, set_working_hours)

    def get_salary(self):
        return self.working_hours * 150.0


class Salesman(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    def set_sales(self, sales):
        self._sales = sales

    def get_sales(self):
        return self._sales

    sales = property(get_sales, set_sales)

    def get_salary(self):
        return 1200.0 + 0.05 * self._sales


def main():
    employees = [Manager('Lee'), Programmer('Chin'), Salesman('On')]
    sum = 0.0

    for employee in employees:
        if isinstance(employee, Programmer):
            employee.working_hours = int(input('input working hours of {}: '\
                .format(employee.get_name())))
        elif isinstance(employee, Salesman):
            employee.sales = int(input('input sales of {}: '\
                .format(employee.get_name())))

        sum += employee.get_salary()
        print('{} get {} yen'.format(employee.name, employee.get_salary()))

    print('the sum of salary is {}'.format(sum))

if __name__ == "__main__":
    main()