# 6! = 1 * 2 * 3 * 4 * 5 * 6
# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9

number = int(input('Введите целое положительное число: '))

count = 1
result = 1
while number >= count:
    if count % 3 == 0:
        count += 1
        continue
    result *= count
    count += 1
    if count > 10:
        break
else:
    print('Факториал меньше 10')

print(result)
