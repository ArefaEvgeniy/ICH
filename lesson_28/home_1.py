# Напишите программу, которая подсчитывает количество вхождений каждого слова
# в тексте и выводит на экран наиболее часто встречающиеся слова. Для решения
# задачи используйте класс Counter из модуля collections. Создайте функцию
# count_words, которая принимает текст в качестве аргумента и возвращает
# словарь с количеством вхождений каждого слова. Выведите наиболее часто
# встречающиеся слова и их количество.
#
# Пример вывода:
# Введенный текст:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

from collections import Counter


def count_words(text):
    t = text.lower().replace(",", "").replace(".", "").split()
    return Counter(t).items()


s = input("Введите текст: ")
c = sorted(count_words(s), key=lambda x: x[1], reverse=True)

for i in c[:2] if len(c) > 2 else c:
    print(f"{i[0]}: {i[1]}")
