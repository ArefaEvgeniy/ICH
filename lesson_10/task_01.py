# Напишите программу, которая запрашивает у пользователя натуральное число N и
# вычисляет сумму первых N элементов ряда Лейбница. Ряд Лейбница представляет
# собой альтернирующийся ряд, где каждый элемент равен (-1)^n / (2n + 1),
# где n - номер элемента (начиная с 0). Выведите результат на экран с помощью
# команды print. Используйте библиотеку decimal для вычисления суммы с большой
# точностью.
# Пример вывода:
# Введите натуральное число N: 1000
# Сумма первых 1000 элементов ряда Лейбница: 0.785647913584885803999456610480

import decimal


while True:
    number = input('Введите натуральное число N: ')
    if number.isdigit() and int(number) != 0:
        number = int(number)
        break
    print('Вы ввели не натурильное число, повторите ввод')

n = 0
result_1 = 0
decimal.getcontext().prec = 30
result_2 = decimal.Decimal('0')
while n < number:
    result_1 += ((-1) ** n) / (2 * n + 1)
    result_2 += decimal.Decimal.from_float(((-1) ** n) / (2 * n + 1))
    n += 1

print('Сумма первых', number, 'элементов ряда Лейбница:', result_1)
print('Сумма первых', number, 'элементов ряда Лейбница:', result_2)
