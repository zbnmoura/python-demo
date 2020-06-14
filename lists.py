# A List is a collection which is ordered and changeable. Allows duplicate members.

# create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['bananas', 'abacaxi', 'coco', 'tomate']

# use a constructor
numbers2 = list((1, 2, 3, 4))

# get a value
print(fruits[0])
# > bananas

# get a length
print(len(fruits))
# > 4

# append to list
fruits.append('uva')
print(fruits)
# > ['bananas', 'abacaxi', 'coco', 'tomate', 'uva']

# remove from list
fruits.remove('bananas')
print(fruits)
# > ['abacaxi', 'coco', 'tomate', 'uva']

# insert into position
fruits.insert(1, 'abacate')
print(fruits)
# > ['abacaxi', 'abacate', 'coco', 'tomate', 'uva']

# remove with pop
fruits.pop(2)
print(fruits)
# > ['abacaxi', 'abacate', 'tomate', 'uva']

# reverse list
fruits.reverse()
print(fruits)
# > ['uva', 'tomate', 'abacate', 'abacaxi']

# sort list
fruits.sort()
print(fruits)
# > ['abacate', 'abacaxi', 'tomate', 'uva']

# reverse sort
fruits.sort(reverse=True)
print(fruits)
# > ['uva', 'tomate', 'abacaxi', 'abacate']