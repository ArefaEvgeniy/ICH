my_dict = {99: 1, 'RR': 20, 0: 'tt', 1: 'EE', 'TT': 0, 5: 1, 3: 3, 2: 22}
my_dict[4] = 44
my_dict.update({'qq': 45, 7: 77})

print(my_dict)

print(my_dict['TT'])
# print(my_dict['TTT'])

print(my_dict.get('TT'))
print(my_dict.get('TTT'))

print(my_dict.get('TT', 99))
print(my_dict.get('TTT', 99))

print('-' * 100)
print(my_dict)

print(my_dict.setdefault('TT'))
print(my_dict.setdefault('TTT'))

print('-' * 100)
print(my_dict)

print(my_dict.setdefault('TT', 99))
print(my_dict.setdefault('TTT', 99))
print(my_dict.setdefault('SSS', 99))

print('-' * 100)
print(my_dict)
