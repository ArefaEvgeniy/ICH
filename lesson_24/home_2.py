# Напишите программу, которая использует рекурсию для вычисления суммы цифр
# числа. Создайте функцию sum_digits, которая принимает один аргумент - число,
# для которого нужно вычислить сумму цифр. Используйте условие выхода из
# рекурсии, когда число состоит из одной цифры. Выведите результат на экран.
#
# Пример вывода:
# Введите число: 12345
# Сумма цифр числа 12345 равна 15

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n//10)


a = int(input("Введите число: "))
print("Сумма цифр: ", sum_digits(a))