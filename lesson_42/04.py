def my_decorator(func):
    def wrapper():
        print('Before func')
        func()
        print('After func')

    return wrapper


@my_decorator
def along_func():
    print('I am along function')


@my_decorator
def along_func_2():
    print('I am along function 2')


@my_decorator
def along_func_3():
    print('I am along function 3')


along_func()
print('-' * 50)
along_func_2()
print('-' * 50)
along_func_3()
