# Дан текстовый файл, где каждая строка описывает человека в формате:
# <Name>; <Age>
# Sergey;35
# Ivan;25
# Svetlana;20
# Maria;27
# Нужно написать программу, которая печатает имя самого старшего человека.
# Поменяйте программу так, чтобы она печатала список людей, чем возраст
# больше 25 лет.


with open("people.txt", "r") as file:
    persons = {item[0]: item[1].strip() for item in map(lambda f: f.split(";").strip(), file.readlines())}

print(max(persons, key=lambda key: persons[key]))
print(list(filter(lambda key: (int(persons[key]) > 25), persons)))
