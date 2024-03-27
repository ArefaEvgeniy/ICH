def my_generator():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
    except GeneratorExit:
        # Код для очистки ресурсов
        pass
    except IndexError:
        yield 44


gen = my_generator()
for item in gen:
    print(item)
    if next(gen) == 2:
        gen.throw(IndexError())
        # raise IndexError()
