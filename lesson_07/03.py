
while True:
    number = int(input('Введите целое положительное число: '))

    count = 1
    result = 1
    while number >= count:
        result *= count
        count += 1
        if count > 10:
            break

    print(result)

    answer = input('Хотите выйти? (y/n)')
    if answer.lower() == 'y':
        break
