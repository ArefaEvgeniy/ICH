my_dict = {"name": "John", "age": 25}
another_dict = dict([("name", "Jane"), ("age", 30), (34, 77)])

print(my_dict)
print(another_dict)

print("name" in my_dict)
print("John" in my_dict)

print('-' * 50)
for item in another_dict:
    print(item)
