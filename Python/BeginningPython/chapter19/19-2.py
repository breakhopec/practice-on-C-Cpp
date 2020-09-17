from configparser import ConfigParser

config = ConfigParser()
config.read('CONFIGURE.ini')

# 三种访问方法
PI = config.getfloat('value', 'PI')
VALUE = config['value'].getint('BUFFSIZE')
description = config['description']['description']
text = config.get('description', 'text')

print('{} {} {} {}'.format(PI, VALUE, description, text))