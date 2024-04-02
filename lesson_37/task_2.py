# У вас есть текстовый файл, где каждая строка - имя человека. Написать
# программу, которая выводит следующее приветствие:
# “Привет, <имя 1>, <имя 2>,... <имя n> и добро пожаловать!”. Программу
# реализовать с помощью генератора и суб-генератора, где суб-генератор
# возвращает имена из файла, а основной генератор в нужный момент считывает
# и возвращает значения из суб-генератора.

def names_generator(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def welcome_message(names_gen):
    names = []
    yield from (", ".join(names + [name]) + " и добро пожаловать!" for name in names_gen)


names_gen = names_generator("names.txt")

for message in welcome_message(names_gen):
    print("Привет,", message)
