# Пример вывода:
# Введите список чисел, разделенных пробелами: -2 5 -8 10 -1 0 7
# Положительные числа из списка: [5, 10, 7]

my_list = input('Введите список чисел, разделенных пробелами: ').split()
new_list = [int(i) for i in my_list if int(i) > 0]

print(new_list)
