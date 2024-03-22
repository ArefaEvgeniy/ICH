# Напишите программу, которая принимает произвольное количество аргументов от
# пользователя и передает их в функцию calculate_sum, которая возвращает сумму
# всех аргументов. Используйте оператор * при передаче аргументов в функцию.
# Выведите результат на экран.
#
# Пример вывода:
# Введите числа, разделенные пробелами: 1 2 3 4 5
# Сумма чисел: 15

def calculate_sum(*s):
    summ = 0
    for i in s:
        summ += i
    return summ


d = list(map(int, input("Введите список чисел: ").split()))
print(calculate_sum(*d))