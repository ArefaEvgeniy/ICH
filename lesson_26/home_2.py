# Напишите программу, которая принимает строку от пользователя и подсчитывает
# количество уникальных символов в этой строке. Создайте функцию
# count_unique_chars, которая принимает строку и возвращает количество
# уникальных символов. Выведите результат на экран.
#
# Пример вывода:
# Введите строку: hello
# Количество уникальных символов: 4

s = set(input("Введите строку: "))
print("Количество уникальных символов: ", len(s))
