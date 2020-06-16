# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#simple if
if x > y:
    print(f'{x} > {y}')

#if/else
if x > y:
    print(f'{x} > {y}')
else:
    print(f'{y} > {x}')

#elif
if x > y:
    print(f'{x} > {y}')
elif x == y:
    print(f'{x} = {y}')
else:
    print(f'{y} > {x}')

#nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

#and
if x > 2 and x <= 10:
    print('and')

#or
if x > 2 or x <= 10:
    print('or')

#not
if not(x == y):
    print('not')



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4]

#in
if x in numbers:
    print(x in numbers)

#not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is
if x is y:
    print(x is y)

#is not
if x is not y:
    print(x is not y)
