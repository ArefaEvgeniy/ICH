def func_1(a='Red'):
    return a + '!'


print(func_1('White'))
print(func_1)

b = func_1

print(b())
del func_1
print(b('White'))
