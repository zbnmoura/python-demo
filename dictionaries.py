# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create dictionarie
person = {
    'first_name': 'joao',
    'last_name': 'da silva',
    'age': 30
}

# create with constructor
person2 = dict(firstname='maria', last_name='da silva', age='30')

# get propertie
print(person['first_name'])
# > joao

print(person2.get('last_name'))
# > da silva

# add key/value
person['email'] = 'joaozinho@gmail.com'

# get keys
print(person.keys())

# get values
print(person.values())

# get items
print(person.items())

# copy dict
person3 = person.copy()
person3['phone'] = '11 934949491'
print(person3)
# > {'first_name': 'joao', 'last_name': 'da silva', 'age': 30, 'email': 'joaozinho@gmail.com', 'phone': '11 934949491'}

# remove item
del(person['age'])
person.pop('first_name')
print(person)
# > {'last_name': 'da silva', 'email': 'joaozinho@gmail.com'}

# clear dict
person.clear()

# get lenght
print(len(person2))
# > 3 

# list of dict
list_of_dict = [
    {'nome':'bozonaru', 'profissao':'residente da replublica'},
    {'nome':'random', 'profissao':'money'}
]
print(list_of_dict)
# > [{'nome': 'bozonaru', 'profissao': 'residente da replublica'}, {'nome': 'random', 'profissao': 'money'}]
print(list_of_dict[0]['nome'])
# > bozonaru