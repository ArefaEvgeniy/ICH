# Реализовать простую поисковую систему.
# Для данных в формате фамилия-имя-год рождения-курс-количество баллов
# реализовать функцию, которой на вход будет приходить поле по которому надо
# искать и значение, которое надо найти. Если есть, то вернуть все подходящие
# записи, если нет – вывести сообщение об ошибке.
# Задача должна работать максимально быстро, при этом использование памяти не
# так важно.

data = [
    {"фамилия": "Иванов", "имя": "Иван", "год": 1990, "курс": 3, "баллы": 75},
    {"фамилия": "Петров", "имя": "Петр", "год": 1988, "курс": 2, "баллы": 82},
    {"фамилия": "Сидоров", "имя": "Александр", "год": 1992, "курс": 4, "баллы": 90},
    {"фамилия": "Иванов", "имя": "Петр", "год": 1993, "курс": 1, "баллы": 68}
]

search_field = "фамилия"
search_value = "Иванов"


def func_1(field_name, value):
    for item in data:
        if item[field_name] == value:
            print(item)


func_1(search_field, search_value)

print('-' * 100)


def create_new_data(data):
    new_data = {}
    for record in data:
        for key, value in record.items():
            if key not in new_data:
                new_data[key] = {}
            if value not in new_data[key]:
                new_data[key][value] = []
            new_data[key][value].append(record)
    return new_data


def func_2(new_data, field_name, value):
    if field_name not in new_data or value not in new_data[field_name]:
        return "Not found"
    for item in new_data[field_name][value]:
        print(item)


new_data = create_new_data(data)

func_2(new_data, search_field, search_value)

print(new_data)
