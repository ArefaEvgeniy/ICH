# Напишите программу, которая принимает список чисел от пользователя и использует
# функцию reduce из модуля functools, чтобы найти произведение всех чисел в списке.
# Затем программа должна использовать функцию itertools.accumulate для накопления
# произведений чисел в новом списке. В результате программа должна вывести список,
# содержащий накопленные произведения.

from functools import reduce
from itertools import accumulate
from operator import mul

numbers = [int(x) for x in input("Введите список чисел: ").split()]
product_red = reduce(lambda x, y: x*y, numbers)
print(product_red)
product_acc = accumulate(numbers, mul)
print(list(product_acc))

