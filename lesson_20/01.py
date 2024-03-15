string_1 = 'Hello {}. Name {} is a ...'
string_2 = 'Hello {1}. Name {3} is a ...'
string_3 = 'Hello {0}. Name {0} is a ...'
string_4 = 'Hello {name_1}. Name {name_2} is a ...'
string_5 = 'Hello %s. Name %s is a ...'

a = 'Bob'
b = 'Tom'

print(string_1.format('Bob', 'Tom'))
print(string_2.format('Bob', 'Tom', 'Jassy', 'Nick'))
print(string_3.format('Bob'))
print(string_4.format(name_2='Bob', name_1='Tom'))
print(f'Hello {a}. Name {b} is a ...')

print(string_5 % (a, 'Tom'))
