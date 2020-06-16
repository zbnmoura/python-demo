# Python has functions for creating, reading, updating, and deleting files.

#open a file
my_file = open('my-file.txt','w')

#get some info
print(f'name: {my_file.name}')
print(f'is closed: {my_file.closed}')
print(f'opening mode: {my_file.mode}')

my_file.write('pyhton is cool')
my_file.write(' with auto append')
my_file.close()

#append to file
my_file = open('my-file.txt', 'a')
my_file.write(' but i prefer be loved')
my_file.close()

#read from file
my_file = open('my-file.txt','r+')
text = my_file.read(100)
print(text)
