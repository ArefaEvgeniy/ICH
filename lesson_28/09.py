import json


my_base = [
    {
        'name': 'Bob',
        'age': 34,
        'maried': False,
        'children': None
    },
    {
        'name': 'Kate',
        'age': 25,
        'maried': True,
        'children': ('Junior', 'Nick')
    }
]

with open('test_2.txt', 'w') as file:
    json.dump(my_base, file)

...

with open('test_2.txt') as file:
    new_data = json.load(file)

print(new_data)
print(type(new_data))
print(my_base)

print(my_base[1].get('children'))

print('-' * 100)

print(new_data[1].get('children'))
