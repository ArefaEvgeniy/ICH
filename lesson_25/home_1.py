# Напишите программу, которая принимает список слов и возвращает список,
# содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента
# и возвращает список анаграмм. Используйте множества и сортировку букв в слове
# для проверки на анаграмму. Выведите результат на экран.
#
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
#
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

def anagrams(x):
    a = []
    for i in s:
        for k in a:
            if sorted(k[0]) == sorted(i):
                k.append(i)
                break
        else:
            a.append([i])
    return a


s = input("Введите список: ").split()
print("Анаграммы: ")
for k in anagrams(s):
    if len(k) > 1:
        print(k)
