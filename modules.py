# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core modules

#import datetime
#today = datetime.date.today()
from datetime import date
today = date.today()
print(today)

#import time
#timestamp = time.time()
from time import time
timestamp = time()
print(timestamp)

#pip modules
from camelcase import CamelCase

c = CamelCase()

print(c.hump('hello world'))

#import custom module
from validator import validate_email

email = 'valid@gmail.com'

if validate_email(email):
    print(f'valid email')
else:
    print('invalid email')
