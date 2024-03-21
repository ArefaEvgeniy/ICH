my_dict = {"name": "John", "age": 25}

print(my_dict)

my_dict["city"] = "New York"  # Добавление элемента
my_dict["name"] = "Bob"
print(my_dict)
del my_dict["age"]  # Удаление элемента по ключу
my_dict.pop("city")  # Удаление элемента с возвратом значения
print(my_dict)
# print(a_1)
