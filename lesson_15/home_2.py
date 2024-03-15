# Напишите программу, которая принимает два списка одинаковой длины и создает
# новый список, содержащий пары элементов из исходных списков. Используйте
# функцию zip() для создания пар элементов. Выведите результат на экран с
# помощью команды print.
#
# Пример вывода:
# Введите элементы первого списка, разделенные пробелом: 1 2 3 4 5
# Введите элементы второго списка, разделенные пробелом: A B C D E
#
# Список пар элементов: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]

x = input("Введите первый список: ").split()
y = input("Введите второй список: ").split()
print("Список пар:", list(zip(x, y)))
