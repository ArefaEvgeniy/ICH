from collections import defaultdict


my_dict = defaultdict(int)
my_dict["apple"] = 6
print(dict(my_dict))
print(my_dict["apple"])    # Выводит 5
print(my_dict["banana"])   # Выводит 0, так как ключа "banana" нет, но defaultdict автоматически создал его со значением 0
print(dict(my_dict))
print(my_dict["banana"])
print(dict(my_dict))
