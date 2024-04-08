def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before func')
        result = func(*args, **kwargs)
        print('After func')
        return result

    return wrapper


@my_decorator
def along_func():
    print('I am along function')


@my_decorator
def along_func_2(a, b):
    print(f'Summa: {a + b}')
    return a + b + 1


along_func()
print('-' * 50)
res = along_func_2(23, 45)
print(res)
