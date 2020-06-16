# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample json
user_json = '{"name":"bruno", "age":27}'

#parse to dict
user = json.loads(user_json)

print(user, type(user))
print(user['name'])

#dict to json(str)
car = {'color':'gray', 'make':'toyota', 'model':'yaris', 'year':2019}

car_json = json.dumps(car)

print(car_json, type(car_json))
