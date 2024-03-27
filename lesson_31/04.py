def my_generator():
    yield 1
    yield 2
    yield 3


def my_func():
    return 1


fun = my_func()
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
for item in gen:
    print(item)
