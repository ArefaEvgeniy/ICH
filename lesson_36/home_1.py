# Напишите функцию, которая принимает на вход список чисел и возвращает сумму
# квадратов только четных чисел из списка, используя функциональные подходы
# (например, map, filter и reduce).
#
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

from functools import reduce


def sq_sum(s):
    filt = filter(lambda x: x % 2 == 0, s)
    sqmap = map(lambda x: x*x, filt)
    sumsq = reduce(lambda x, y: x+y, sqmap)
    return sumsq


i = map(int, input("Введите список чисел: ").split(", "))
print(sq_sum(i))
