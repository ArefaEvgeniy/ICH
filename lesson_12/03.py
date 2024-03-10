str_1 = 'Hello, world!'
str_2 = 'world.'
str_3 = '12345'

print(str_1.endswith('world!'))
print(str_2.endswith('world!'))
print(str_3.endswith('world!'))

print('-' * 50)

a = '1'
print(str_1.startswith(a))
print(str_2.startswith(a))
print(str_3.startswith(a))

print('-' * 50)

string = input('Enter yor string: ')

print(string.endswith(','))
