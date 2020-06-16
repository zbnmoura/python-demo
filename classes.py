# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'my name is {self.name} and iam {self.age}'

    def has_birthday(self):
        self.age += 1

#extend class
class Customer(User):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
#overwrite User greeting
    def greeting(self):
        return f'my name is {self.name} and iam {self.age} and my balance is {self.balance}'

#init user object
bruno = User('bruninho', 'bruninho@gmail.com', 27)
bruno.has_birthday()
print(bruno.greeting())

#init customer object
tobias = Customer('tovias', 'tobias@gmail.com', 29)
tobias.set_balance(2)

print(tobias.greeting())
