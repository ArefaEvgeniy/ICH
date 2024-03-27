my_list = [5, 7, 99, 0, 112, 1]
my_iter = iter(my_list)

print(my_list)
print(type(my_list))
print(my_iter)
print(type(my_iter))

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))

print('-' * 50)
for item in my_list:
    print(item)

numbers = range(1, 1001)
print(numbers)
