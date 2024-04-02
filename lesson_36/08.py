numbers = [0, 1, 2, 3, 4, 5]
squared = filter(lambda x: x % 2 == 0, numbers)
print(list(squared))


def my_func(x):
    return x % 2 == 0


squared_2 = filter(my_func, numbers)
print(list(squared_2))
