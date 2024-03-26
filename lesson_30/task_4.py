# Напишите функцию, которая получает на вход две строки с перечислением
# интересов и хобби двух пользователей, и вычисляет процент совпадения.
# Использовать множества.

def perc(str1, str2):

    str1 = set(str1.split(', '))
    str2 = set(str2.split(', '))

    str3 = str1.intersection(str2)

    a = len(str1) + len(str2)

    percent = len(str3) / a * 2 * 100
    return percent


x1 = 'a, b, c, d, f'
x2 = 'a, o, i, h, j'

print(f'{perc(x1, x2)}%')
