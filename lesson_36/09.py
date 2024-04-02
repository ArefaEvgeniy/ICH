from functools import reduce

numbers = [0, 1, 2, 3, 4, 5]
squared = reduce(lambda x, y: x + y ** 2, numbers)
print(squared)


def my_func(x, y):
    return x + y ** 2


squared_2 = reduce(my_func, numbers)
print(squared_2)
