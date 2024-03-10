# Напишите программу, которая запрашивает у пользователя вещественное число и
# выводит его представление в памяти компьютера. Вещественные числа в памяти
# компьютера представлены с использованием формата с плавающей запятой.
# Используйте стандартные функции языка Python для получения представления
# числа в бинарном виде и вывода его на экран.
# Пример вывода:
# Введите десятичное число: 3.14
# Представление числа в формате IEEE 754: 01000000010010001111010111000010

number = float(input("Введите десятичное число: "))

# Проверяем знак числа
sign_repr = '1' if number < 0 else '0'
number = abs(number)

# Отделяем целую часть от дробной
integer_number = int(number)
fractional_number = number - integer_number

# Преобразуем целую часть в бинарное представление
integer_binary = bin(integer_number)[3:]

degree = len(integer_binary)

exponent = 127 + degree
exponent_repr = bin(exponent)[2:]

# Преобразуем дробную часть в бинарное представление
fractional_binary = ''
count = 24
while fractional_number > 0 and count > 0:
    count -= 1
    # Умножаем дробную часть на 2
    fractional_number *= 2
    # Если результат больше или равен 1, добавляем 1 к дробной части и вычитаем 1
    if fractional_number >= 1:
        fractional_binary += '1'
        fractional_number -= 1
    else:
        fractional_binary += '0'

# Собираем бинарное представление числа
binary_number = sign_repr + exponent_repr + integer_binary + fractional_binary

print('Представление числа в формате IEEE 754:', binary_number)
