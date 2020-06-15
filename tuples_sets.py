# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create a tuple
fruits = ('banana', 'pera', 'abacate')

#  with constructor
fruits2 = tuple(('banana', 'pera', 'abacate'))

# single value needs trailing comma, or will be a string
fruits3 = ('single value',)

# get value
print(fruits[1])
# > pera

# cant change value
# fruits[1] = 'impossible'

# delete tuple
del fruits2
# print(fruits2)
# > NameError: name 'fruits2' is not defined

# get lenght
print(len(fruits))
# > 3


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'banana', 'tomate', 'manga'}

# check if in set
print('banana' in fruits_set)
# > True

# add to set
fruits_set.add('uva')
print(fruits_set)
# > {'tomate', 'uva', 'manga', 'banana'}

# add duplicate
fruits_set.add('uva')
print(fruits_set)
# ? if already exists will not duplicate ?
# > {'tomate', 'uva', 'manga', 'banana'}

# remove from set
fruits_set.remove('uva')
print(fruits_set)
# > {'manga', 'banana', 'tomate'}

# clear set
fruits_set.clear()
print(fruits_set)
# > set()

# delete set
del fruits_set
# print(fruits_set)
# > NameError: name 'fruits_set' is not defined
