# Напишите программу, которая запрашивает у пользователя два числа и выводит
# их сумму и произведение в следующем формате:
# "Сумма: {sum:.2f}, Произведение: {product:.2f}"
#
# Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения,
# округленные до двух десятичных знаков. Используйте f-строки с использованием
# форматных спецификаторов для форматирования чисел. Выведите результат на
# экран с помощью команды print.
#
# Пример вывода:
# Введите первое число: 3.14159
# Введите второе число: 2.71828
#
# Сумма: 5.86, Произведение: 8.54

x = float(input("Введите первое число:"))
y = float(input("Введите второе число:"))
sum = x + y
product = x * y
print(f"Сумма: {sum:.2f}, Произведение: {product:.2f}")
