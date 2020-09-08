'''
    伪代码
'''

dish.get('ham')
dish.add('ham', 'eggs')
if dish.is_hot():
    dish.add('pepper')
while dish.status:
    dish.cook()
    if dish.cooktime() % 10 == 0:
        dish.status = dish.is_raw()