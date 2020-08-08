#coding=utf-8
#swap in and cm

value = float(input('input value:'))
unit = input('input unit:')

if unit == 'in':
    print('%fin=%.2fcm' % (value,value*2.54))
elif unit == 'cm':
    print('%fcm=%.2fin' % (value,value/2.54))
else:
    print('Please input valid unit')