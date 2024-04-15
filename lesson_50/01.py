import sqlite3

import query


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
    return result


connection = create_connection("sm_app.sqlite")

# execute_query(connection, query.create_users_table)
# execute_query(connection, query.create_posts_table)
# execute_query(connection, query.create_comments_table)
# execute_query(connection, query.create_likes_table)
#
# execute_query(connection, query.create_users)
# execute_query(connection, query.create_posts)
# execute_query(connection, query.create_comments)
# execute_query(connection, query.create_likes)

# users_posts = execute_read_query(connection, query.select_users_posts)
# for users_post in sorted(users_posts, reverse=True):
#     print(users_post)
#
# print('-' * 100)
#
# post_likes = execute_read_query(connection, query.select_post_likes)
# for post_like in post_likes:
#     print(post_like)

# post_description = execute_read_query(connection, query.select_post_description)
# print(post_description)
#
# execute_query(connection, query.update_post_description)
# post_description = execute_read_query(connection, query.select_post_description)
# print(post_description)

# execute_query(connection, query.delete_comment)

execute_query(connection, query.delete_comment_table)

connection.close()
