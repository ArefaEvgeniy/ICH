def my_generator():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
    except GeneratorExit:
        print('CLOSE GENERATOR')
        pass


gen = my_generator()
for item in gen:
    if item == 3:
        gen.close()
    print(item)

print('-' * 50)
print(next(gen))
