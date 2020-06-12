# strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'bruninho'
age = 27

# concatenate
print('hello, my name is ' + name + ' and i am ' + str(age))
# > hello, my name is bruninho and i am 27  


# arguments by position
print('my name is {name} and iam {age}'.format(name=name, age=age))
# > my name is bruninho and iam 27

# f-Strings
print(f'hi, my name is {name} and iam {age}')
# > hi, my name is bruninho and iam 27


# string Methods

s = 'hello WORLD'

# capitalize string
print(s.capitalize())
# > Hello world

# all uppercase
print(s.upper())
# > HELLO WORLD

#all lower
print(s.lower())
# > hellow world

# swap case
print(s.swapcase())
# > HELLO world

# get length
print(len(s))
# > 11

# replace
print(s.replace('hello','hero'))
# > hero WORLD

# count
o = 'o'
print(s.count(o))
# > 1

# start with
print(s.startswith('hello'))
# > True

# ends with
print(s.endswith('d'))
# > False

# split into a list
print(s.split())
# > ['hello', 'WORLD']

# find position
print(s.find('r'))
# > -1

# is all alphanumeric
print(s.isalnum())
# > False

# is all alphabetic
print(s.isalpha())
# > False

# is all numeric
print(s.isnumeric())
# > False
