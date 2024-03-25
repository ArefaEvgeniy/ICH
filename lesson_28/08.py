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

with open('test_1.txt', 'w') as file:
    file.write(str(my_base))

...

with open('test_1.txt') as file:
    new_data = file.read()

print(new_data)
print(type(new_data))

print(my_base[1].get('children'))

print('-' * 100)

print(new_data[:20])
