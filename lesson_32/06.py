def my_generator():
    value = yield
    if value > 0:
        yield value * 2
    else:
        yield value * 3


gen = my_generator()
print(next(gen))
# print(gen.send(15))
# print(gen.send(-4))
print(gen.send(0))
