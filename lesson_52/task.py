import const
from bd import get_connection, execute_query


def prepare_categoris(data):
    data_print = []
    categories = []
    for id_cat, name in data:
        categories.append(int(id_cat))
        data_print.append(f'{id_cat:3}  -{name:^15}')
    data_print = '\n'.join(data_print)
    return data_print, categories


def input_category(categories):
    while True:
        category = input('Выдерите категорию: ')
        if not category.isdigit() or int(category) not in categories:
            print('Ошибка, повторите ввод')
        else:
            break
    return category


def print_data(category, connection):
    query = const.QUERY_FILMS.format(category)
    data = execute_query(connection, query)
    if data is not None:
        print('-' * 150)
        print('   Название фильма   |  Год | Описание')
        print('-' * 150)
        for name, year, description in data:
            print(f'{name[:20]:>20} |{year:^6}| {description[:100]}')


def main():
    connection = get_connection()
    if connection is None:
        return None

    data = execute_query(connection, const.QUERY_CATEGOTIES)
    data_print, categories = prepare_categoris(data)
    while True:
        print(data_print)
        category = input_category(categories)
        print_data(category, connection)

        if input('Хотите выйти? (Д/Y)').lower() in ('д', 'y'):
            print('До свидания\nРабота программы завершена')
            break

    connection.close()


main()
