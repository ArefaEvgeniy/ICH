def sub_generator():
    yield 'Sub generator'
    yield 'Next sub generator'
    yield 'Completed sub generator'


def main_generator():
    yield 'Main generator'
    yield from sub_generator()
    yield 'Next main generator'
    yield from sub_generator()
    yield 'Completed main generator'


gen = main_generator()
# for item in gen:
#     print(item)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
