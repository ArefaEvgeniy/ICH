my_dict = {"name": "John", "age": 25, "city": "New York"}

print(my_dict)
print(list(my_dict.items()))
print(list(my_dict.keys()))
print(list(my_dict.values()))

print('-' * 50)
for item in my_dict:
    print(my_dict[item])

print('-' * 50)
for item in my_dict.values():
    print(item)

print('-' * 50)
for item in my_dict.keys():
    print(item)

print('-' * 50)
for key, value in my_dict.items():
    print('key:', key)
    print('value:', value)
