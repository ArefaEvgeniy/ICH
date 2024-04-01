numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))


def my_func(x):
    return x ** 2


squared_2 = map(my_func, numbers)
print(list(squared_2))
