from functools import partial

func_1 = lambda x, y: x * y

print(func_1(10, 5))
print(func_1(10, 8))

print("-" * 50)
func_2 = partial(lambda x, y: x * y, 10)

print(func_2(5))
print(func_2(8))
