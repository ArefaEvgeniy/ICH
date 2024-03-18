def my_func(e, a, *args):
    print('e:', e)
    print('a:', a)
    print('args:', args)


a = 0
b = 10
my_func(a, b, 'TTT', 44, 345, 66.778, 112, 89087, 'sdfsd', 'rrr')
my_func(a, b, 'TTT')
my_func(a, b)

print('-' * 50)


def my_func_2(*args):
    print('args:', args)


my_func_2()
my_func_2(a)
my_func_2(a, b)
my_func_2(a, b, 'TTT')


def my_func_3(*args):
    return min(args)


print(my_func_3(1))
print(my_func_3(1, -45, 100, 56))
print(my_func_3(1, 5, 0, 44))
