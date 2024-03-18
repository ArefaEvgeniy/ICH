def summa(a, b):
    return a + b


print(summa(3, 4))

add = lambda x, y: x + y
print(add(3, 4))


def func(n, start, even=False):
    result = []
    for item in range(start, n+1):
        if even is False and item % 2 == 0:
            continue
        result.append(item ** 2)

    return result


print(func(10, 3, even=True))
print(func(4, 1))

func_l = lambda n, start, even=False: [i**2 for i in range(start, n+1)
                                       if not (even is False and i % 2 == 0)]

print(func_l(10, 3, even=True))
print(func_l(4, 1))
