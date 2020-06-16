# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['dudu', 'emilia', 'floki', 'duque']

#simple for loop

for person in people:
    print(f'simple {person}')

#with break
for person in people:
    if person == 'floki':
        break
    print(f'break {person}')

#with continue
for person in people:
    if person == 'dudu':
        continue
    print(f'continue {person}')

#range
for i in range(0, 10):
    print(f'range {i}')


# While loops execute a set of statements as long as a condition is true.
count = 0
while count < 10:
    print(f'while {count}')
    count += 1

