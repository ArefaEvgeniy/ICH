import const
from bd import get_connection, execute_read_query


def prepare_categories(data):
    categories = []
    result = []
    for number, name in data:
        result.append(f'{number:3}   -{name:^15}')
        categories.append(int(number))
    result = '\n'.join(result)
    return result, categories


def validation(input_data, categories):
    result = None
    if input_data.isdigit() and int(input_data) in categories:
        result = int(input_data)
    return result


def print_data(category, connection):
    data = execute_read_query(connection, const.QUERY_FILMS, category)
    print('   Название фильма    |  Год | Описание')
    print('-' * 150)
    for item in data:
        print(f'{item[0][:21]:>21} |{item[1]:^6}| {item[2]}')


def main():
    connection = get_connection()

    if connection:
        while True:
            data = execute_read_query(connection, const.QUERY_CATEGORIES)
            data_to_print, categories = prepare_categories(data)
            print(data_to_print)
            if not (category := validation(input('Выберите категорию: '), categories)):
                print('Ошибка, повторите ввод')
                continue

            print_data(category, connection)

            if input('Хотите выйти? (Д/Y)').lower() in ('y', 'д'):
                print(f"До свидания!\nРабота программы завершена")
                break
            print('\n\n')

        connection.close()


main()
