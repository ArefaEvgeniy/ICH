# Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет
# содержать информацию о продукте в формате "название, цена, количество".

# Пример:
# Apple, 1.50, 10
# Banana, 0.75, 15

# В программе определите функцию calculate_total_price, которая будет принимать
# список продуктов и возвращать общую стоимость. Продумайте, какая аннотация
# должна быть у аргумента. Считайте данные из файла, разделите строки на
# составляющие и создайте список продуктов. Вызовите функцию
# calculate_total_price с этим списком и выведите результат.

from typing import List, Tuple


def calculate_total_price(c: List[Tuple[str, float, int]]) -> float:
    total = 0
    for i in c:
        total += i[1] * i[2]
    return total


# def calculate_total_price(product_list: List[Tuple[str, float, int]]) -> float:
#     return sum([price * amount for name, price, amount in product_list])


f = [x.split(", ") for x in open("products.txt", "r").readlines()]
s = [(y[0], float(y[1]), int(y[2])) for y in f]
print(calculate_total_price(s))
