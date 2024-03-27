my_list = [1, 2, 3]
for item in my_list:
    print(item)

print('-' * 50)

iterator = iter(my_list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

