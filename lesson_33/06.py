from operator import add, sub, mul, truediv


def func(a, b, operation):
    return operation(a, b)


print(func(6, 7, mul))
print(func(6, 7, add))
print(func(6, 7, truediv))


print(add(5, 3))     # Результат: 8
print(sub(10, 2))    # Результат: 8
print(mul(2, 4))    # Результат: 8
print(truediv(16, 2))  # Результат: 8.0

print('-' * 50)

print(add(5, 3))
print(5 + 3)
