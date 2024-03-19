# Дано предложение из слов, разделенных пробелами. Написать функцию transform(),
# которая принимает такое предложение и возвращает аналогичное, но где все
# слова длиной 3 символа в этом предложении написаны заглавными буквами.
# Пример: “The quick brown fox jumps over the lazy dog” ->
# “THE quick brown FOX jumps over THE lazy DOG”.
#
# *Дополнительное не обязательное к выполнению задание:
# Функция должна принимать 2 дополнительных параметра в виде лямбда-функций.
# Первая лямбда-функция - это условие, к примеру - если длина слова 4 символа
# или если слово начинается на заглавную букву или если всё слово из строчных
# букв и т.д. Вторая лямбда-функция - это действие которое необходимо применить.
# К примеру - удалить данное слово, заменить все его буквы на знак "*" или
# сделать все буквы слова заглавными и т.д.


def transform(string, func_1, func_2):
    new_list = string.split()

    for i, item in enumerate(new_list):
        if func_1(item):
            new_list[i] = func_2(item)
    return " ".join(new_list)


string = "The quick brown fox jumps over the lazy dog"

print(transform(string, lambda item: len(item) == 5, lambda item: "*"*len(item)))
