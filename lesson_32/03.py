def fibonacci_generator():
    try:
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    except GeneratorExit:
        pass


fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))
# for i in fib_gen:
#     print(i)

fib_gen.close()
# fib_gen.throw(GeneratorExit())

print('-' * 100)
print(next(fib_gen))
print(next(fib_gen))
