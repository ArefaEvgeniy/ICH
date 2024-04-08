def along_func():
    print('I am along function')


def my_decorator(func):
    def wrapper():
        print('Before func')
        func()
        print('After func')

    return wrapper


# along_func()
# print('-' * 50)
along_func = my_decorator(along_func)
along_func()
