# Предоставлен список натуральных чисел. Требуется сформировать из них
# множество. Если какое-либо число повторяется, то преобразовать его в строку
# по образцу: например, если число 4 повторяется 3 раза, то в множестве будет
# следующая запись: само число 4, строка 44 (второе повторение, т.е. число
# дублируется в строке), строка 444 (третье повторение, т.е. строка множится
# на 3). Реализуйте вывод множества через функцию set_gen().

from collections import Counter

numbers = [1, 3, 4, 4, 6, 7, 7, 7, 4, 3]


def set_gen(numbers):
    num_set = set()
    num_dict = Counter(numbers)
    for key, value in num_dict.items():
        if value > 1:
            num_set.add(str(key) * value)
        else:
            num_set.add(key)
    return num_set


print(set_gen(numbers))
