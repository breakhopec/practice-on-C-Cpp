#coding=utf-8

meals = ('meal1', 'meal2', 'meal3', 'meal4', 'meal5')

for meal in meals:
    print(meal, end=' ')
#error
#maels[0] = 'meal6'
temp_list = list(meals)
temp_list[0] = 'meal6'
meals = tuple(temp_list)
print('')
print(meals)