import mysql.connector

import const


def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**const.DB_CONFIG)
        print("Соединение с БД прошло успешно")
    except mysql.connector.Error as e:
        print(f"Ошибка при соединении с БД: '{e}'")
        print(f"Работа программы завершена")
    return connection


def execute_read_query(connection, query, data=None):
    cursor = connection.cursor()
    result = None
    try:
        if data is not None:
            query = query.format(data)
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Ошибка '{e}' при осуществлении запроса:\n{query}")
    finally:
        cursor.close()
    return result
