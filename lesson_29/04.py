def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль недопустимо")
    return x / y


print(divide(2, 0))
