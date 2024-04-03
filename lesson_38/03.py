from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
print(result)

result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)


result = filter(lambda x: int(x) % 2 == 0, reduce(lambda x, y: str(x) + str(y), map(lambda x: x ** 2, numbers)))  # [1, 4, 9, 16, 25] -> '1491625' -> ['4', '6', '2']
print(list(result))
