from functools import partial


def func_1(a, b, c, d=1):
    print(a)
    print(b)
    print(c)
    print(d)
    return a + b + c + d


func_2 = partial(func_1, 0, 2)


print(func_1(2, 3, 4))
print('-' * 50)
print(func_2(5, 6))
