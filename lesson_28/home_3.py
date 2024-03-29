# Напишите программу, которая принимает словарь от пользователя и ключ, и
# возвращает значение для указанного ключа с использованием метода get или
# setdefault. Создайте функцию get_value_from_dict, которая принимает словарь
# и ключ в качестве аргументов, и возвращает значение для указанного ключа,
# используя метод get или setdefault в зависимости от выбранного варианта.
# Выведите полученное значение на экран.
#
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
#
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

def get_value_from_dict(dict, key, method):
    if method:
        return dict.get(key)
    return dict.setdefault(key, 0)


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

k = input("Введите ключ для поиска: ")
m = True if input("Использовать метод get (y/n)? ").lower() == "y" else False

print(f"Значение для ключа '{k}': {get_value_from_dict(my_dict, k, m)}")
